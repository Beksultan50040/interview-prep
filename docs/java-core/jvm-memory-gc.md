# JVM, memory and GC

## Key concepts

- **JDK vs JVM vs JRE:** the JDK is the development kit (compiler, tools, runtime); the JVM executes bytecode; the JRE is the traditional name for the runtime part. Bytecode is platform-independent and lives in `.class` files.
- **Pipeline:** `javac` produces bytecode, the JVM loads classes on demand, links and initializes them, interprets the bytecode, and JIT-compiles hot code. The GC reclaims unreachable heap objects.
- **Specification vs implementation:** the JVM spec defines behavior; layout and GC algorithms are implementation choices. These notes describe HotSpot (OpenJDK, Oracle JDK).
- **Class loading:** bootstrap, platform, application loaders; parent delegation; why classloader leaks happen in app servers.
- **JIT:** interpreter, C1 and C2 tiers, inlining, escape analysis. Warm-up matters for benchmarks (use JMH).
- **Java Memory Model:** happens-before rules define visibility and ordering. See [Concurrency](concurrency.md).

## Runtime memory areas

| Area | Scope | Holds | Notes |
|---|---|---|---|
| Heap | Shared | Objects and arrays | Managed by GC; young (eden + survivors) and old |
| Java stack | Per thread | Frames: locals, operand stack | One frame per call, dropped on return |
| PC register, native stack | Per thread | Execution position, native calls | |
| Metaspace | Shared, native memory | Class metadata | HotSpot's implementation of the method area; PermGen was removed in Java 8 |
| Code cache, direct buffers, thread stacks | Native memory | JIT code, NIO buffers | Not limited by `-Xmx` |

### Heap vs stack

- A local variable holds a **reference** in the stack frame; the object it points to lives on the heap.
- Each thread has its own stack, but threads share heap objects, which is why thread safety matters.
- Deep or infinite recursion exhausts the stack: `StackOverflowError`.
- "Objects always live on the heap" is a model: escape analysis and scalar replacement can remove an allocation entirely.
- Static fields belong to the class, but the objects they reference (for example a static `HashMap` and its entries) are heap objects.

## Generations and GC phases

- **Why generational:** most objects die young (request DTOs, strings, temporary collections), while caches live for hours. Collecting the young area often is cheap; survivors are promoted to the old generation.
- **Not a fixed layout:** G1 is region-based and regions change roles. Eden/S0/S1/Old is a model, not contiguous spaces for every collector.
- **Reachability:** the GC traces references from **GC roots** (thread stacks, static and native references). Objects with no path from a root are eligible. Eligible does not mean collected immediately.
- **Phases (conceptual):** identify live objects, reclaim the rest, optionally compact or copy survivors.
- **Young vs old collection:** young collections are frequent and cheap when most objects are dead; old collections cost more as the live graph grows.
- **Stop-the-world (STW):** application threads pause for GC work, which shows up as request latency or timeouts. Concurrent collectors still have short pauses and use CPU while running.

## Garbage collectors

| GC | Good for | Notes |
|---|---|---|
| Serial | Tiny heaps, single core | Single GC thread, stop-the-world |
| Parallel | Throughput batch jobs | Multiple GC threads, longer pauses |
| G1 (default since 9) | General purpose, balanced | Region-based, pause-time goal via `-XX:MaxGCPauseMillis` |
| ZGC | Very low latency, large heaps | Concurrent, sub-millisecond pauses; generational mode since 21 |
| Shenandoah | Low latency | Concurrent compaction |

### Choosing a collector

- Start from measured goals: throughput (work completed), latency (pause times and p99), or memory limits (heap, native memory, container).
- For a typical Spring Boot service on Java 17+, G1 is a sensible default. Change it only when measurements show a need.
- A low-pause collector does not make every application faster; it trades CPU and memory.
- If there is a problem, investigate before touching collector settings.

## Memory leaks in Java

- A leak means objects stay **reachable** but are no longer useful, so the GC cannot reclaim them.
- Typical causes: unbounded static caches or maps, listeners never deregistered, long-lived objects holding large graphs, thread locals in pools.
- Fix by bounding or evicting (size limits, TTL, weak references) and by controlling who holds references.

## JVM flags and container memory

| Option | Meaning |
|---|---|
| `-Xms` | Initial heap size |
| `-Xmx` | Maximum heap size |
| `-Xss` | Thread stack size (more threads means more memory) |
| `-XX:+UseG1GC` | Select G1 |
| `-Xlog:gc*` | Detailed GC logging (unified logging) |
| `-XX:MaxRAMPercentage` | Heap as a share of container memory |

- Example: `java -Xms512m -Xmx2g -Xlog:gc* -jar app.jar`.
- `-Xmx` limits the **heap**, not the process. Metaspace, thread stacks, code cache and direct buffers come on top.
- A container can hit its memory limit while heap usage is below `-Xmx`. Make sure the JVM is container-aware.

## OutOfMemoryError and StackOverflowError

| Error | Meaning | Typical cause |
|---|---|---|
| `OutOfMemoryError: Java heap space` | Heap allocation cannot be satisfied | Unbounded cache, leak, heap too small |
| `OutOfMemoryError: Metaspace` | Class metadata cannot be allocated | Excessive class generation, classloader retention |
| `OutOfMemoryError: unable to create native thread` | OS or JVM cannot create another thread | Too many threads, native resource limits |
| `StackOverflowError` | A thread's stack is full | Infinite or very deep recursion |

Do not infer the cause from the name alone; read the full message and surrounding logs.

### Diagnosing an OOM in production

1. **Identify the failing resource:** full exception, surrounding logs, container events, JVM memory settings.
2. **Look at the trend:** continuous growth, spikes under traffic, or a stable level after GC.
3. **Capture evidence:** GC logs, heap dump, thread dump, Native Memory Tracking.
4. **Find the cause:** retained objects and reference chains, collection sizes, allocation hotspots, thread counts, native usage.
5. **Fix and verify:** remove unintended retention or excess allocation, change limits only when justified, re-test under realistic load.

### Typical scenarios

| Scenario | Symptom | Investigate |
|---|---|---|
| Object retention | Memory stays high after GC | Heap dump, dominator tree, retained heap, cache eviction |
| High allocation rate | Frequent GC, memory drops after each | JFR allocation profiling, GC logs, request workload |
| Native memory pressure | Heap looks fine, process or container grows | Container metrics, thread count, Native Memory Tracking, direct buffers |

Raising `-Xmx` may delay a leak, does not fix it, may not help native memory at all, and can worsen container pressure.

## Troubleshooting toolbox

- `jcmd <pid> GC.heap_dump`, `jcmd <pid> Thread.print`, `jstack`, `jmap`
- Java Flight Recorder and JDK Mission Control
- GC logs: `-Xlog:gc*`
- Eclipse MAT for dominator tree and GC roots
- Async-profiler for CPU and allocation flame graphs

!!! warning "Production diagnostics"
    Heap dumps can be large, pause the application, and contain sensitive data. Store and share them carefully.

## Common questions

- What is the difference between the JDK and the JVM?
- Heap vs stack: what lives where?
- How does the GC decide an object is garbage? (Reachability from GC roots, not reference counting.)
- Why can a Java application leak memory?
- Young collection vs old-generation collection?
- What causes `OutOfMemoryError: Java heap space` vs `Metaspace` vs `unable to create native thread`?
- Why can a container run out of memory while heap usage is below `-Xmx`?
- How would you investigate continuously increasing memory usage?
- Strong, soft, weak, phantom references: when would you use each?
- What is a safepoint and why does it matter for pauses?

!!! warning "Gotchas and interview traps"
    - "Java has no leaks because of GC": false, unwanted references keep objects alive.
    - "All variables are on the stack": false, references are; objects are (conceptually) on the heap.
    - "GC deletes unreachable objects immediately": false, eligibility is not collection.
    - "Only the heap matters": false, native memory and thread stacks cause production failures.
    - "More heap is always faster": false, it can mean longer full GCs and more memory use.
    - "Every GC stops all threads": false, collectors work concurrently but still have pause phases.
    - "Metaspace is the new heap": false, it is a separate native-memory area for class metadata.
    - Excessive allocation in hot paths is often the real cause of GC pressure, not the GC settings.

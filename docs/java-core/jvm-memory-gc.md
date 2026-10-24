# JVM, memory and GC

## Key concepts

- **Memory areas:** heap (young: eden + survivors, old), metaspace (class metadata, native memory), thread stacks, code cache, direct buffers.
- **Class loading:** bootstrap, platform, application loaders; parent delegation; why classloader leaks happen in app servers.
- **JIT:** interpreter, C1 and C2 tiers, inlining, escape analysis. Warm-up matters for benchmarks (use JMH).
- **Java Memory Model:** happens-before rules define visibility and ordering. See [Concurrency](concurrency.md).

## Garbage collectors

| GC | Good for | Notes |
|---|---|---|
| Serial | Tiny heaps, single core | Stop-the-world |
| Parallel | Throughput batch jobs | Longer pauses |
| G1 (default since 9) | General purpose, balanced | Region-based, pause-time goal via `-XX:MaxGCPauseMillis` |
| ZGC | Very low latency, large heaps | Concurrent, sub-millisecond pauses; generational mode since 21 |
| Shenandoah | Low latency | Concurrent compaction |

## Common questions

- How does GC decide an object is garbage? (Reachability from GC roots, not reference counting.)
- What causes `OutOfMemoryError: Java heap space` vs `Metaspace` vs `unable to create native thread`?
- Strong, soft, weak, phantom references: when would you use each?
- How would you find a memory leak? (Heap dump, Eclipse MAT, JFR, look at dominator tree and GC roots.)
- What is a safepoint and why does it matter for pauses?

## Troubleshooting toolbox

- `jcmd <pid> GC.heap_dump`, `jcmd <pid> Thread.print`, `jstack`, `jmap`
- Java Flight Recorder and JDK Mission Control
- GC logs: `-Xlog:gc*`
- Async-profiler for CPU and allocation flame graphs

!!! warning "Gotchas"
    - Bigger heap is not always better: longer full GCs, more cache misses.
    - In containers, make sure the JVM is container-aware (`-XX:MaxRAMPercentage`).
    - Excessive allocation in hot paths is often the real cause of GC pressure, not the GC settings.

# Question bank

Add every question you meet, from interviews or practice, with your own short answer. Mark how well you know it.

Legend: strong, medium, weak.

## Java core

| Question | Short answer | Level |
|---|---|---|
| How does `HashMap` handle collisions? | Bucket list, treeified at 8 entries when the table is at least 64 | strong |
| What does `volatile` guarantee? | Visibility and ordering, not atomicity | strong |
| Difference between G1 and ZGC? | G1 balances throughput and pauses; ZGC targets sub-millisecond pauses on large heaps | medium |
| What is the difference between the JDK and the JVM? | The JDK is the dev kit (compiler, tools, runtime); the JVM executes bytecode and manages runtime resources | weak |
| What is the difference between heap and stack? | Heap: shared, holds objects, GC-managed. Stack: per thread, holds frames with locals and references; frames dropped on return | weak |
| How does the JVM decide which objects can be collected? | Reachability from GC roots (thread stacks, statics, native refs); unreachable objects are eligible, not collected immediately | weak |
| Why can a Java application have a memory leak? | Objects stay reachable (static cache, listeners, long-lived holders) but are no longer needed, so GC cannot reclaim them | weak |
| Young GC vs old-generation collection? | Young: frequent, cheap when most objects die young; old: holds survivors, costs more as live data grows | weak |
| Why can a container run out of memory below `-Xmx`? | `-Xmx` limits only the heap; Metaspace, thread stacks, code cache and direct buffers add native memory | weak |
| How do you investigate continuously growing memory? | Identify the failing resource, check the trend, capture GC logs/heap dump/NMT, find the cause, fix and verify under load | weak |

## Spring and data

| Question | Short answer | Level |
|---|---|---|
| Why does `@Transactional` fail on self-invocation? | The call bypasses the proxy | strong |
| How do you fix the N+1 problem? | `JOIN FETCH`, entity graphs, batch fetch, DTO projections | strong |

## Architecture

| Question | Short answer | Level |
|---|---|---|
| What is the outbox pattern? | Write the event in the same DB transaction, publish it asynchronously | medium |

## Add new questions here

| Question | Short answer | Level |
|---|---|---|
| | | |

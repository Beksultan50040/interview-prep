# Concurrency

## Key concepts

- **Visibility, atomicity, ordering:** the three problems the memory model addresses.
- **`volatile`:** visibility and ordering, not atomicity (`count++` is still unsafe).
- **`synchronized`:** mutual exclusion plus happens-before on the same monitor.
- **`java.util.concurrent`:** `ExecutorService`, `ConcurrentHashMap`, `CopyOnWriteArrayList`, `BlockingQueue`, `CountDownLatch`, `Semaphore`, `ReentrantLock`, `StampedLock`, atomics (`AtomicInteger`, `LongAdder`).
- **`CompletableFuture`:** composition of async steps; always pass a dedicated executor for blocking work.
- **Virtual threads (Java 21):** cheap threads for blocking IO; do not pool them; avoid pinning (long `synchronized` blocks with blocking calls).

## Deadlock, livelock, starvation

- Deadlock needs: mutual exclusion, hold and wait, no preemption, circular wait. Break one of them, for example by always acquiring locks in a consistent order.
- Detect with `jstack` or `jcmd Thread.print`.

## Thread pools

```java
ExecutorService pool = new ThreadPoolExecutor(
    4, 16, 60, TimeUnit.SECONDS,
    new ArrayBlockingQueue<>(100),
    new ThreadPoolExecutor.CallerRunsPolicy());
```

- Core size, max size, queue and rejection policy interact: threads above core are only created when the queue is full.
- Size CPU-bound pools near the core count; IO-bound pools bigger, or use virtual threads.

## Common questions

- Difference between `ConcurrentHashMap` and `Collections.synchronizedMap`?
- How does `ConcurrentHashMap` work in Java 8+? (CAS plus per-bin synchronization, treeified bins.)
- `ReentrantLock` vs `synchronized`: when choose the lock? (tryLock, fairness, interruptible, multiple conditions.)
- What is false sharing? (Threads writing different variables on the same cache line; see `@Contended`.)
- How do you make a class immutable and why does it help?
- Explain `ThreadLocal` risks in thread pools and with virtual threads.

!!! warning "Gotchas"
    - Double-checked locking requires `volatile`.
    - `parallelStream()` uses the common ForkJoin pool; blocking tasks can starve everything else.
    - Swallowed exceptions in executor tasks: use `Future.get()` or an uncaught exception handler.

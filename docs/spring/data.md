# Transactions, JPA and SQL

## Transactions

- **ACID** and isolation levels: read uncommitted, read committed, repeatable read, serializable.
- Anomalies: dirty read, non-repeatable read, phantom read, lost update, write skew.
- **Propagation:** `REQUIRED` (default), `REQUIRES_NEW`, `NESTED`, `SUPPORTS`, `NEVER`.
- Spring rolls back on unchecked exceptions by default; checked exceptions need `rollbackFor`.
- Optimistic locking (`@Version`) vs pessimistic locking (`SELECT ... FOR UPDATE`).
- Distributed consistency: outbox pattern, sagas, idempotent consumers. See [Microservices](../architecture/microservices.md).

## JPA and Hibernate

- Entity states: transient, managed, detached, removed. First-level cache is per persistence context.
- **N+1 problem:** fix with `JOIN FETCH`, entity graphs, batch fetching, or DTO projections.
- `LAZY` vs `EAGER`: prefer lazy everywhere; beware `LazyInitializationException` and open-session-in-view.
- `equals` and `hashCode` on entities: use a business key or a stable id strategy.
- `@OneToMany` with `mappedBy`; bidirectional helper methods to keep both sides in sync.
- Bulk updates bypass the persistence context.
- Flush modes and when Hibernate flushes (before queries, on commit).

## SQL

- Index types: B-tree (default), hash, composite (leftmost prefix rule), covering indexes, partial indexes.
- Read query plans with `EXPLAIN ANALYZE`; look for seq scans, bad estimates, sorts spilling to disk.
- Joins, window functions (`ROW_NUMBER`, `LAG`), CTEs, `GROUP BY` with `HAVING`.
- Pagination: offset gets slow on deep pages; use keyset pagination.
- Connection pooling (HikariCP): size pool small, near `cores * 2 + effective spindles` as a starting point.
- Schema migration: Flyway or Liquibase; expand and contract for zero downtime.

## Common questions

- Explain isolation levels with an example anomaly each.
- How would you debug a slow query in production?
- When do you pick NoSQL over a relational database?
- How do you handle schema changes with no downtime?
- Caching strategy: cache-aside, write-through, invalidation, stampede protection.

# System design

## Framework for the interview (about 45 minutes)

1. **Clarify requirements** (5 min): functional, non-functional (latency, availability, consistency, scale), what is out of scope.
2. **Estimate** (5 min): requests per second, storage, bandwidth. Rough numbers are fine.
3. **API and data model** (5 min): main endpoints, entities, access patterns.
4. **High-level design** (10 min): clients, load balancer, services, database, cache, queue.
5. **Deep dive** (15 min): the hardest part (hot spots, consistency, scaling the data layer).
6. **Trade-offs and failure modes** (5 min): what breaks, how you monitor, what you would improve.

## Building blocks

- Load balancing (L4 vs L7), CDN, reverse proxy
- Caching: client, CDN, application, database; eviction (LRU, TTL); invalidation
- Databases: replication, sharding (hash vs range), partition keys, secondary indexes
- CAP and PACELC: the trade-off between consistency and availability during partitions, and latency otherwise
- Queues and streams for decoupling and smoothing load
- Rate limiting: token bucket, leaky bucket, sliding window
- Unique id generation: UUID, Snowflake-style ids
- Search (inverted index), blob storage, notifications

## Practice problems

- [ ] URL shortener
- [ ] Rate limiter
- [ ] News feed or timeline
- [ ] Chat system
- [ ] Notification service
- [ ] File storage and sharing
- [ ] Payment processing (idempotency, ledger)
- [ ] Distributed job scheduler

!!! tip
    Say your assumptions out loud, and when you pick a technology, name one alternative and why you did not choose it.

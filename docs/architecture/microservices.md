# Microservices and messaging

## When microservices make sense

Independent deployability, clear domain boundaries, multiple teams. Costs: network failures, distributed data, operational overhead. A modular monolith is often the better starting point.

## Key concepts

- **Service boundaries:** domain-driven design, bounded contexts, own your data (database per service).
- **Communication:** REST, gRPC, async messaging. Prefer async for decoupling and resilience.
- **Resilience:** timeouts, retries with backoff and jitter, circuit breaker, bulkhead, rate limiting (Resilience4j).
- **Consistency:** eventual consistency, saga (orchestration vs choreography), outbox pattern, idempotency keys.
- **API design:** versioning, pagination, idempotent methods, error model, backward compatibility.
- **Observability:** structured logs with correlation ids, metrics, distributed tracing (OpenTelemetry).
- **Deployment:** containers, Kubernetes basics, health probes, config and secrets, blue-green and canary releases.

## Messaging and Kafka

- Topic, partition, offset, consumer group. Ordering is guaranteed only within a partition.
- Delivery semantics: at-most-once, at-least-once (default practical choice), exactly-once (transactions plus idempotent producers, with limits).
- Make consumers idempotent; use a dead letter topic for poison messages.
- Partition key choice drives ordering and load distribution (hot partitions).
- Consumer lag is the key operational metric.
- Compare with RabbitMQ: smart broker, routing, queues vs a distributed log.

## Common questions

- How do you handle a distributed transaction across services?
- How do you avoid duplicate processing?
- How do you version an API without breaking clients?
- What is the outbox pattern and what problem does it solve? (Atomically updating the DB and publishing an event.)
- How do you test microservices? (Unit, contract tests with Pact, component tests, few end-to-end.)

!!! warning "Gotchas"
    - Retries without idempotency cause duplicates.
    - Synchronous call chains multiply latency and failure probability.
    - Shared databases between services create hidden coupling.

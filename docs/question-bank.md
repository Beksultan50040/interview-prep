# Question bank

Add every question you meet, from interviews or practice, with your own short answer. Mark how well you know it.

Legend: strong, medium, weak.

## Java core

| Question | Short answer | Level |
|---|---|---|
| How does `HashMap` handle collisions? | Bucket list, treeified at 8 entries when the table is at least 64 | strong |
| What does `volatile` guarantee? | Visibility and ordering, not atomicity | strong |
| Difference between G1 and ZGC? | G1 balances throughput and pauses; ZGC targets sub-millisecond pauses on large heaps | medium |

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

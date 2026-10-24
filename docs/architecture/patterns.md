# Design principles and patterns

## SOLID

- **S**ingle responsibility: one reason to change.
- **O**pen/closed: extend by adding code, not editing stable code.
- **L**iskov substitution: subtypes must honor the base contract.
- **I**nterface segregation: small focused interfaces.
- **D**ependency inversion: depend on abstractions; the basis of DI.

## Other principles

- Composition over inheritance, DRY (but avoid premature abstraction), KISS, YAGNI, Law of Demeter.
- Clean and hexagonal architecture: domain at the center, adapters at the edges.

## Patterns to know well

| Category | Patterns | Typical Java or Spring example |
|---|---|---|
| Creational | Factory, Builder, Singleton | `Optional.of`, Lombok builders, Spring beans |
| Structural | Adapter, Decorator, Proxy, Facade | `InputStreamReader`, Spring AOP proxies |
| Behavioral | Strategy, Observer, Template method, Chain of responsibility | `Comparator`, Spring events, servlet filters |

## Common questions

- Implement a thread-safe singleton (enum or holder idiom) and explain the pitfalls.
- Strategy vs State?
- Give an example where you refactored toward a pattern, and one where a pattern was overkill.
- Explain dependency injection without a framework.

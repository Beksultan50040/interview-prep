# Modern Java (8 to 21)

## Java 8

- Lambdas, functional interfaces, method references
- Streams: lazy, single-use, avoid side effects; know `collect`, `groupingBy`, `flatMap`, `reduce`
- `Optional`: for return types, not fields or parameters
- `java.time` API, default methods

## Java 9 to 17

- Modules (JPMS), `List.of`, `var` (10), text blocks (15)
- Records (16): immutable data carriers; compact constructors; not a replacement for entities
- Sealed classes (17): restricted hierarchies, work well with pattern matching
- Pattern matching for `instanceof` (16)
- `HttpClient` (11)

## Java 18 to 21

- Switch expressions and pattern matching for `switch` (21)
- Record patterns (21)
- Virtual threads (21), structured concurrency and scoped values (preview)
- Sequenced collections (21), generational ZGC (21)

```java
sealed interface Shape permits Circle, Rect {}
record Circle(double r) implements Shape {}
record Rect(double w, double h) implements Shape {}

double area(Shape s) {
    return switch (s) {
        case Circle c -> Math.PI * c.r() * c.r();
        case Rect r -> r.w() * r.h();
    };
}
```

## Common questions

- Streams vs loops: readability, performance, debugging?
- When are records a bad fit? (JPA entities, mutable state.)
- How do virtual threads differ from platform threads, and when do they not help? (CPU-bound work.)
- What is the difference between `Optional.orElse` and `orElseGet`?

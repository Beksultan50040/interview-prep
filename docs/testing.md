# Testing

## Strategy

- **Test pyramid:** many fast unit tests, fewer integration tests, very few end-to-end tests.
- Test behavior, not implementation. Avoid over-mocking.
- Deterministic tests: control time, randomness, and external systems.

## Tools

- JUnit 5, AssertJ, Mockito
- Spring: `@SpringBootTest`, slice tests (`@WebMvcTest`, `@DataJpaTest`), MockMvc
- Testcontainers for real databases and brokers in integration tests
- Contract testing: Pact or Spring Cloud Contract
- Performance: JMH (microbenchmarks), Gatling or k6 (load)
- Mutation testing: PIT

## Common questions

- Mock vs stub vs spy vs fake?
- How do you test code that uses time or randomness?
- How do you keep integration tests fast and reliable?
- What is a flaky test, and how do you handle it?
- What would you test first in a legacy codebase with no tests? (Characterization tests around the riskiest paths.)

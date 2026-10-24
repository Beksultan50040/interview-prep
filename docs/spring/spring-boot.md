# Spring and Spring Boot

## Key concepts

- **IoC container and DI:** prefer constructor injection; makes dependencies explicit and testable.
- **Bean lifecycle:** instantiate, populate, `BeanPostProcessor`, `@PostConstruct`, ready, `@PreDestroy`.
- **Scopes:** singleton (default), prototype, request, session. Singletons must be stateless or thread-safe.
- **AOP and proxies:** `@Transactional`, `@Async`, `@Cacheable` work through proxies (JDK or CGLIB). **Self-invocation bypasses the proxy.**
- **Auto-configuration:** `@SpringBootApplication` = `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`; conditions like `@ConditionalOnClass` and `@ConditionalOnMissingBean`.
- **Configuration:** profiles, `application.yml`, `@ConfigurationProperties`, externalized config and secrets.
- **Web:** `DispatcherServlet` flow, filters vs interceptors, exception handling with `@ControllerAdvice`, validation with Bean Validation.
- **Actuator and observability:** health, metrics (Micrometer), tracing.
- **Security:** filter chain, authentication vs authorization, JWT and OAuth2 resource server basics.

## Common questions

- How does Spring resolve circular dependencies? Why avoid them?
- Why does `@Transactional` on a private or self-invoked method not work?
- `@Component` vs `@Bean`? `@Autowired` field vs constructor?
- How would you design a global error response format?
- MVC vs WebFlux: when would you pick reactive? (High concurrency IO with a fully non-blocking stack; virtual threads reduce the need.)
- How do you write a custom starter?

!!! warning "Gotchas"
    - Large `@Transactional` scopes hold DB connections and cause pool exhaustion.
    - `@Async` without a configured executor uses a simple executor in some setups; define your own.
    - Startup time and memory: lazy init, class data sharing, GraalVM native images as options.

# Project-Based System Design Roadmap

**Learner profile:** intermediate developer  
**Study time:** 2 hours daily, approximately 14 hours weekly  
**Length:** 24 weeks  
**Goal:** design, implement, explain, and defend production-style HLD and LLD systems.

## Source video and verification

The primary source is [Complete System Design Roadmap 2026 | HLD & LLD by Shradha Ma'am](https://www.youtube.com/watch?v=CuQmQpvw04I). Its chapter list verifies the main sequence: system design, HLD, LLD, fundamentals, databases, consistency and availability, caching, networking, load balancers, message queues, monoliths versus microservices, monitoring and logging, security, trade-offs, a Netflix example, OOP, design patterns, concurrency, UML, APIs, and common LLD problems. A timestamped companion summary provides additional detail for scaling, replication, sharding, cache policies, rate limiting, RabbitMQ, Docker, monitoring tools, authentication, authorization, and encryption: [timestamped summary](https://videohighlight.com/v/CuQmQpvw04I).

The chapter timestamps are:

| Time | Video-verified topic |
|---|---|
| 00:32 | What is system design? |
| 01:12 | High-Level Design |
| 01:36 | Low-Level Design |
| 02:35 | HLD discussion |
| 04:19 | Basic fundamentals |
| 05:56 | Databases |
| 06:43 | Consistency and availability |
| 08:16 | Caching |
| 09:30 | Networking |
| 10:03 | Load balancers |
| 10:27 | Message queues |
| 11:08 | Monoliths versus microservices |
| 11:55 | Monitoring and logging |
| 12:44 | Security |
| 13:07 | System design trade-offs |
| 15:39 | Netflix HLD example |
| 16:53 | LLD discussion |
| 16:58 | OOP concepts |
| 17:16 | Design patterns |
| 17:34 | Concurrency and thread safety |
| 17:56 | UML diagrams |
| 18:20 | APIs |
| 18:46 | Common LLD problems |

Topics marked **[Added]** are recommendations needed for a complete intermediate roadmap: capacity estimation, DNS, CDNs, indexes, replication, sharding, consistent hashing, idempotency, distributed locks, observability, disaster recovery, testing, and cost estimation.

## Core materials

- [System Design Primer](https://github.com/donnemartin/system-design-primer): free reference covering scalability, databases, caching, queues, protocols, security, HLD exercises, and LLD exercises.
- [Gaurav Sen / InterviewReady notes](https://interviewready.io/system-design-notes): structured video path using an e-commerce system, then networks, databases, consistency, messaging, WhatsApp, Instagram, Uber, and rate limiting.
- [Gaurav Sen playlist index](https://tutorialtube.online/playlist/system-design-playlist/): short videos on scaling, load balancing, consistent hashing, queues, microservices, and distributed systems.
- [Designing Data-Intensive Applications](https://dataintensive.net/): deeper material on storage, replication, partitioning, consistency, and stream processing.
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/the-pillars-of-the-framework.html): review every project against operational excellence, security, reliability, performance, cost, and sustainability.
- [Google SRE book](https://sre.google/sre-book/table-of-contents/): reliability, monitoring, incident response, capacity, and distributed systems.
- [ByteByteGo YouTube](https://www.youtube.com/@ByteByteGo): visual explanations and design walkthroughs.
- [Hussein Nasser YouTube](https://www.youtube.com/@hnasr): networking, databases, proxies, and backend internals.
- [Exponent YouTube](https://www.youtube.com/@tryexponent): mock interviews and complete design answers.
- [Refactoring Guru](https://refactoring.guru/design-patterns): design patterns and OOP.

## Weekly routine

Use 35 minutes for learning, 45 minutes for implementation or diagramming, 25 minutes for questions, and 15 minutes for review. Every week should produce a diagram, a short written design, and one measurable implementation result.

## 24-week sequence

### Weeks 1–2 — Requirements, HLD, LLD, and estimation

**Learn:** functional and non-functional requirements, latency, throughput, availability, scalability, SLAs/SLOs, vertical/horizontal scaling, stateless services, capacity estimation, and architecture diagrams.

**Project:** URL shortener. Define APIs, estimate QPS/storage/bandwidth, choose a database, and document failure cases.

**Practice questions:** What is HLD versus LLD? How do you estimate QPS? Why are stateless services easier to scale? What is an SLO? What is a single point of failure?

**Answer walkthroughs:** [URL shortener design videos](https://www.youtube.com/results?search_query=system+design+URL+shortener+Gaurav+Sen+ByteByteGo), [capacity estimation videos](https://www.youtube.com/results?search_query=system+design+back+of+the+envelope+capacity+estimation).

### Weeks 3–4 — Networking and APIs

**Learn:** DNS, IPs, ports, TCP/UDP, TLS, HTTP/1.1–HTTP/3, REST, RPC, gRPC, WebSockets, polling, reverse proxies, CDNs, timeouts, retries, and connection pooling.

**Project:** REST API behind a reverse proxy. Add HTTPS, timeouts, retries, health checks, and request tracing.

**Materials:** [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview), [Hussein Nasser networking videos](https://www.youtube.com/@hnasr), [DNS and HTTP answer videos](https://www.youtube.com/results?search_query=system+design+DNS+HTTP+TCP+UDP+Hussein+Nasser).

**Practice questions:** What happens after entering a URL? TCP versus UDP? What is a reverse proxy? When should you use WebSockets? Why can retries make an outage worse?

### Weeks 5–6 — Databases and data modeling

**Learn:** SQL, NoSQL, key-value/document/graph stores, indexes, transactions, ACID, normalization, denormalization, read/write workloads, and migrations.

**Project:** E-commerce data model with users, products, inventory, carts, orders, and payments. Add indexes and justify each one.

**Materials:** [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html), [MongoDB data modeling](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/), [database design videos](https://www.youtube.com/results?search_query=system+design+SQL+NoSQL+database+indexing+transactions).

**Practice questions:** When should SQL be preferred? What does an index improve? Why can too many indexes hurt? Explain ACID. Why should payment data normally favor strong consistency?

### Weeks 7–8 — Replication, partitioning, and sharding

**Learn:** primary/replica replication, synchronous/asynchronous replication, lag, partitioning, sharding, federation, consistent hashing, hot partitions, rebalancing, and quorum reads/writes.

**Project:** Multi-region user database. Start with one database, add replicas, then shard by user ID. Simulate a failed primary and an overloaded shard.

**Materials:** [DDIA](https://dataintensive.net/), [consistent hashing videos](https://www.youtube.com/results?search_query=Gaurav+Sen+consistent+hashing+system+design), [database sharding videos](https://www.youtube.com/results?search_query=system+design+database+replication+sharding+ByteByteGo).

**Practice questions:** What is replication lag? What makes a good shard key? What is a hot shard? What is consistent hashing? How does rebalancing work?

### Weeks 9–10 — Consistency and distributed systems

**Learn:** CAP theorem, strong/eventual/read-after-write/causal consistency, quorum, consensus overview, clocks, idempotency, duplicate processing, and conflict resolution.

**Project:** Payment ledger plus notification system. Use strong consistency and idempotency for payments; use eventual consistency for notifications.

**Materials:** [DDIA](https://dataintensive.net/), [CAP and consistency videos](https://www.youtube.com/results?search_query=system+design+CAP+theorem+eventual+consistency+Gaurav+Sen), [distributed systems videos](https://www.youtube.com/results?search_query=distributed+systems+consensus+idempotency+system+design).

**Practice questions:** What does CAP say? When is eventual consistency acceptable? Why is exactly-once difficult? How do idempotency keys prevent duplicate payments? Why are timestamps insufficient for ordering?

### Weeks 11–12 — Caching and performance

**Learn:** cache-aside, read-through, write-through, write-back, write-around, TTL, LRU/LFU, invalidation, stampedes, hot keys, Redis, and CDN caching.

**Project:** Add Redis to the e-commerce service. Measure latency before and after caching, add invalidation, and simulate cache failure.

**Materials:** [Redis documentation](https://redis.io/docs/latest/develop/), [ByteByteGo caching videos](https://www.youtube.com/results?search_query=ByteByteGo+caching+cache+invalidation+LRU+system+design), [cache strategies in the Primer](https://github.com/donnemartin/system-design-primer#cache).

**Practice questions:** What is cache-aside? What is a cache stampede? Compare LRU and LFU. How do you protect a hot key? What happens if Redis is unavailable?

### Weeks 13–14 — Load balancing, rate limiting, and resilience

**Learn:** round-robin, least connections, weighted routing, health checks, stateful/stateless balancing, token bucket, leaky bucket, circuit breakers, bulkheads, and backpressure.

**Project:** Three API instances behind a load balancer with health checks, a distributed rate limiter, and circuit breaking.

**Materials:** [NGINX load balancing](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/), [rate limiting videos](https://www.youtube.com/results?search_query=ByteByteGo+rate+limiter+token+bucket+leaky+bucket), [load balancing videos](https://www.youtube.com/results?search_query=Gaurav+Sen+load+balancing+system+design).

**Practice questions:** How does a load balancer detect failure? Token bucket versus leaky bucket? What is a circuit breaker? What is backpressure? Why can retries amplify failure?

### Weeks 15–16 — Queues and event-driven systems

**Learn:** synchronous/asynchronous work, producers, consumers, queues, pub/sub, RabbitMQ, Kafka, delivery guarantees, consumer groups, ordering, retries, and dead-letter queues.

**Project:** Order-processing pipeline for email, inventory, billing, and analytics. Add retries, idempotent consumers, monitoring, and a dead-letter queue.

**Materials:** [RabbitMQ tutorials](https://www.rabbitmq.com/tutorials), [Kafka documentation](https://kafka.apache.org/documentation/), [message queue videos](https://www.youtube.com/results?search_query=Gaurav+Sen+message+queue+RabbitMQ+Kafka+system+design).

**Practice questions:** Queue versus pub/sub? What is a consumer group? How do you preserve ordering? What is at-least-once delivery? When should Kafka be preferred over RabbitMQ?

### Weeks 17–18 — Monoliths, microservices, and API architecture

**Learn:** modular monoliths, service boundaries, API gateways, service discovery, distributed transactions, Saga, versioning, authentication, authorization, and Docker.

**Project:** Split the e-commerce monolith into catalog, order, payment, and notification services. Document new failure modes and operational costs.

**Materials:** [Martin Fowler microservices](https://martinfowler.com/articles/microservices.html), [Docker getting started](https://docs.docker.com/get-started/), [microservices answer videos](https://www.youtube.com/results?search_query=Gaurav+Sen+microservices+architecture+API+gateway+Saga).

**Practice questions:** When is a monolith better? What makes a good service boundary? What problems do microservices introduce? What is Saga? Authentication versus authorization?

### Weeks 19–20 — Observability, security, and operations

**Learn:** structured logs, metrics, traces, correlation IDs, golden signals, dashboards, alerts, OAuth/JWT, encryption, secrets, DDoS protection, input validation, and threat modeling.

**Project:** Add logs, metrics, tracing, authentication, role-based authorization, and alerts for latency, errors, saturation, and queue growth.

**Materials:** [Google SRE monitoring](https://sre.google/sre-book/monitoring-distributed-systems/), [OWASP API Security Top 10](https://owasp.org/API-Security/), [AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html), [observability answer videos](https://www.youtube.com/results?search_query=system+design+monitoring+logging+distributed+tracing+Prometheus+Grafana).

**Practice questions:** What are the four golden signals? Why do correlation IDs matter? Where should secrets be stored? Encryption at rest versus in transit? What is least privilege?

### Weeks 21–22 — LLD, OOP, patterns, concurrency, and UML

**Learn:** encapsulation, abstraction, inheritance, polymorphism, SOLID, Factory, Strategy, Observer, Builder, Adapter, Decorator, Repository, thread safety, race conditions, locks, deadlocks, and UML.

**Project:** Parking lot and elevator systems. Add a notification service using Strategy and Observer. Make seat booking thread-safe.

**Materials:** [Refactoring Guru patterns](https://refactoring.guru/design-patterns), [PlantUML](https://plantuml.com/guide), [LLD parking lot videos](https://www.youtube.com/results?search_query=low+level+design+parking+lot+system+design), [concurrency videos](https://www.youtube.com/results?search_query=system+design+concurrency+thread+safety+race+condition+deadlock).

**Practice questions:** Explain Single Responsibility. Strategy versus inheritance? What is a race condition? What is a deadlock? How would you make seat booking thread-safe?

### Weeks 23–24 — Capstones and interview simulation

Choose two: Netflix, YouTube, WhatsApp, Uber, Instagram, Twitter/X, Dropbox, a payment system, notification system, or autocomplete.

For each, cover requirements, estimates, APIs, data model, architecture, scaling, caching, consistency, failure recovery, observability, security, and trade-offs.

**Video answer collections:** [Netflix system design](https://www.youtube.com/results?search_query=Netflix+system+design+interview+answer), [YouTube system design](https://www.youtube.com/results?search_query=YouTube+system+design+interview+answer), [WhatsApp system design](https://www.youtube.com/results?search_query=WhatsApp+system+design+interview+answer), [Uber system design](https://www.youtube.com/results?search_query=Uber+system+design+interview+answer), [Instagram system design](https://www.youtube.com/results?search_query=Instagram+system+design+interview+answer), [mock system design interviews](https://www.youtube.com/@tryexponent).

## Concept-by-concept handbook

The weekly plan gives the order. This section explains what each concept means, why it exists, what decision it helps you make, and where to study it on YouTube or in documentation.

### 1. Functional and non-functional requirements

**Summary:** Functional requirements describe what the product does: create an order, send a message, upload a file, or search for a video. Non-functional requirements describe how well it must do it: latency, availability, durability, security, cost, and scale.

**Why it matters:** A design cannot be judged without knowing the target. A chat app may prioritize low latency, while a payment system prioritizes correctness and auditability.

**Common mistake:** Starting with databases or microservices before asking who uses the system, what actions matter, and what failure is acceptable.

**Watch:** [Requirements and system design interviews](https://www.youtube.com/results?search_query=system+design+functional+non+functional+requirements+interview).

### 2. HLD and LLD

**Summary:** High-Level Design describes services, databases, queues, caches, traffic flow, and deployment boundaries. Low-Level Design describes classes, interfaces, methods, relationships, patterns, and thread safety.

**Trade-off:** HLD optimizes system behavior and operational boundaries; LLD optimizes code structure and changeability. Strong design connects both: an HLD service should have a coherent internal model.

**Watch:** [HLD versus LLD](https://www.youtube.com/results?search_query=HLD+vs+LLD+system+design+interview).

### 3. Latency, throughput, availability, and scalability

**Summary:** Latency is the time for one request. Throughput is work completed per unit time. Availability is the percentage of time the service can successfully respond. Scalability is the ability to handle more load by adding resources or changing architecture.

**Key idea:** Improving throughput does not automatically improve tail latency. Always discuss average latency and p95/p99 latency.

**Watch:** [Latency, throughput, availability, and scalability](https://www.youtube.com/results?search_query=system+design+latency+throughput+availability+scalability).

### 4. Capacity estimation

**Summary:** Capacity estimation converts product assumptions into approximate requests per second, storage, bandwidth, memory, and machine count.

**Method:** Estimate users → active users → actions per user → requests per action → peak multiplier → storage growth → bandwidth. Round aggressively; the goal is to expose bottlenecks, not predict the future perfectly.

**Watch:** [Back-of-the-envelope estimation](https://www.youtube.com/results?search_query=system+design+back+of+the+envelope+capacity+estimation).

### 5. Vertical and horizontal scaling

**Summary:** Vertical scaling gives one machine more CPU, memory, or storage. Horizontal scaling adds more machines and distributes requests.

**Trade-off:** Vertical scaling is simple but has hardware limits and a larger failure blast radius. Horizontal scaling improves capacity and redundancy but requires load balancing, statelessness, coordination, and operational tooling.

**Watch:** [Vertical versus horizontal scaling](https://www.youtube.com/results?search_query=Gaurav+Sen+vertical+horizontal+scaling).

### 6. Stateless services

**Summary:** A stateless service does not keep user session state only in its local memory or disk. Any instance can handle any request.

**Why it matters:** Statelessness makes horizontal scaling, rolling deployments, and failover easier. Store shared state in a database, cache, or object store.

**Watch:** [Stateless architecture](https://www.youtube.com/results?search_query=stateless+services+system+design+scalability).

### 7. DNS

**Summary:** DNS maps names such as `api.example.com` to IP addresses or other records. Resolvers and clients cache answers according to TTL.

**Trade-off:** Longer TTL reduces lookup traffic but slows failover and makes changes visible more slowly. DNS can support geographic routing, but it is not a replacement for application-level health checks.

**Material:** [MDN DNS](https://developer.mozilla.org/en-US/docs/Glossary/DNS) · [DNS system design video search](https://www.youtube.com/results?search_query=DNS+system+design+Hussein+Nasser).

### 8. TCP, UDP, HTTP, TLS, and WebSockets

**Summary:** TCP provides reliable ordered delivery. UDP provides low-overhead datagrams without delivery guarantees. HTTP defines request/response semantics. TLS provides confidentiality and server authentication. WebSockets provide a persistent two-way connection.

**Choice:** Use HTTP for ordinary APIs, WebSockets for live bidirectional updates, and UDP-based protocols where latency matters more than built-in reliability.

**Material:** [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) · [Networking explanations](https://www.youtube.com/@hnasr).

### 9. REST, RPC, gRPC, and API design

**Summary:** REST models resources over HTTP. RPC models calling a remote method. gRPC uses strongly typed contracts and efficient binary serialization, often for internal services.

**Good API design:** Define resource names, authentication, pagination, validation, error formats, idempotency keys, versioning, and rate limits.

**Watch:** [REST versus gRPC](https://www.youtube.com/results?search_query=REST+vs+gRPC+system+design+API).

### 10. Reverse proxies and CDNs

**Summary:** A reverse proxy sits in front of application servers and can terminate TLS, route traffic, compress responses, enforce limits, and hide internal topology. A CDN caches content near users.

**Trade-off:** Caching reduces origin load and latency but creates staleness and invalidation problems. Dynamic personalized responses require careful cache keys.

**Material:** [NGINX reverse proxy and load balancing](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/) · [CDN videos](https://www.youtube.com/results?search_query=CDN+reverse+proxy+system+design).

### 11. SQL databases, NoSQL databases, and data modeling

**Summary:** SQL databases provide relational modeling, transactions, joins, and strong constraints. NoSQL systems trade some relational flexibility for simpler horizontal scaling, specialized access patterns, or flexible schemas.

**Decision rule:** Start from access patterns and correctness requirements, not from technology popularity. Model the data around the queries the product must serve.

**Material:** [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) · [MongoDB data modeling](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/) · [SQL versus NoSQL videos](https://www.youtube.com/results?search_query=SQL+vs+NoSQL+system+design+interview).

### 12. Indexes and transactions

**Summary:** An index creates an additional lookup structure so the database can find rows without scanning everything. A transaction groups operations into an atomic unit.

**Trade-off:** Indexes speed reads but consume storage and slow writes. Transactions improve correctness but can reduce throughput and create contention.

**Watch:** [Indexes and transactions](https://www.youtube.com/results?search_query=database+indexes+transactions+system+design+interview).

### 13. Replication

**Summary:** Replication keeps copies of data on multiple nodes. Synchronous replication waits for replicas before acknowledging; asynchronous replication acknowledges sooner but may lose recent writes during failure.

**Important failure:** Replica lag can cause a user to read stale data immediately after writing. Decide whether a particular read needs a primary, a session-consistent replica, or eventual consistency.

**Watch:** [Database replication](https://www.youtube.com/results?search_query=database+replication+system+design+Gaurav+Sen).

### 14. Partitioning, sharding, and consistent hashing

**Summary:** Partitioning splits data into smaller pieces. Sharding distributes those pieces across machines. Consistent hashing reduces the number of keys that move when nodes are added or removed.

**Trade-off:** Sharding increases capacity but makes joins, transactions, rebalancing, and hotspot prevention more difficult. A bad shard key can overload one shard.

**Watch:** [Sharding and consistent hashing](https://www.youtube.com/results?search_query=consistent+hashing+database+sharding+ByteByteGo+Gaurav+Sen).

### 15. CAP theorem and consistency models

**Summary:** During a network partition, a distributed system must choose between returning consistent results and remaining available for all requests. Strong consistency makes reads reflect the latest accepted write. Eventual consistency allows temporary divergence while replicas converge.

**Design use:** Payments and inventory reservations usually need stronger guarantees than likes, view counts, recommendations, or notifications.

**Material:** [DDIA](https://dataintensive.net/) · [CAP theorem videos](https://www.youtube.com/results?search_query=CAP+theorem+strong+eventual+consistency+system+design).

### 16. Idempotency and duplicate processing

**Summary:** An operation is idempotent when repeating it produces the same final result as performing it once. Clients send an idempotency key; the server stores the result for that key and returns it on retries.

**Why it matters:** Networks fail after a server commits but before the client receives the response. Without idempotency, retrying a payment or order can create duplicates.

**Watch:** [Idempotency in payment systems](https://www.youtube.com/results?search_query=system+design+idempotency+payment+duplicate+requests).

### 17. Caching

**Summary:** A cache stores frequently requested data closer to the application or user. Cache-aside loads data on a miss and writes it back to the cache; write-through updates the cache and database together.

**Trade-off:** Caches reduce latency and database load but introduce stale data, invalidation, eviction, memory cost, and failure modes such as stampedes and hot keys.

**Material:** [Redis documentation](https://redis.io/docs/latest/develop/) · [Caching videos](https://www.youtube.com/results?search_query=ByteByteGo+cache+invalidation+cache+stampede+LRU+LFU).

### 18. Load balancers

**Summary:** A load balancer distributes requests among healthy service instances. Algorithms include round-robin, least connections, weighted routing, and consistent-hash routing.

**Design questions:** How are unhealthy instances removed? Is the service stateless? Is session affinity really necessary? What happens when a whole zone fails?

**Material:** [NGINX load balancing](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/) · [Load balancer videos](https://www.youtube.com/results?search_query=Gaurav+Sen+load+balancer+system+design).

### 19. Rate limiting and backpressure

**Summary:** Rate limiting protects a service by restricting requests per user, IP, token, or tenant. Token bucket allows bursts up to bucket capacity; leaky bucket drains at a steady rate. Backpressure slows producers when consumers cannot keep up.

**Trade-off:** A centralized limiter is easier to reason about but can become a bottleneck. Distributed limiters need shared state, clock care, and a decision about fail-open versus fail-closed behavior.

**Watch:** [Rate limiter design](https://www.youtube.com/results?search_query=ByteByteGo+rate+limiter+token+bucket+system+design).

### 20. Message queues and pub/sub

**Summary:** A queue decouples producers from consumers and lets work happen asynchronously. Pub/sub sends an event to multiple subscribers. Kafka is optimized for durable ordered event streams; RabbitMQ is commonly used for brokered work queues and routing.

**Trade-off:** Queues improve resilience and smooth bursts but introduce delayed results, retries, duplicates, ordering concerns, and operational complexity.

**Material:** [RabbitMQ tutorials](https://www.rabbitmq.com/tutorials) · [Kafka documentation](https://kafka.apache.org/documentation/) · [Message queue videos](https://www.youtube.com/results?search_query=Gaurav+Sen+message+queue+RabbitMQ+Kafka).

### 21. Monoliths and microservices

**Summary:** A monolith deploys one application; a modular monolith can still have clean internal boundaries. Microservices split independently deployable services around business capabilities.

**Trade-off:** Microservices can scale teams and components independently, but introduce network failures, distributed tracing, deployment coordination, data ownership, and distributed transactions. Prefer a modular monolith until independent scaling or ownership is worth the cost.

**Material:** [Martin Fowler on microservices](https://martinfowler.com/articles/microservices.html) · [Monolith versus microservices videos](https://www.youtube.com/results?search_query=monolith+vs+microservices+system+design+Gaurav+Sen).

### 22. Distributed transactions and Saga

**Summary:** A distributed transaction spans multiple services or databases. The Saga pattern breaks it into local transactions with compensating actions when a later step fails.

**Example:** Reserve inventory → authorize payment → create shipment. If payment fails, release inventory. A Saga is not magic rollback; compensation may itself fail and must be observable and retryable.

**Watch:** [Saga pattern system design](https://www.youtube.com/results?search_query=Saga+pattern+distributed+transactions+system+design).

### 23. Monitoring, logging, metrics, and tracing

**Summary:** Logs describe events, metrics quantify behavior, and traces connect one request across services. The four common golden signals are latency, traffic, errors, and saturation.

**Practice:** Add a correlation ID, structured JSON logs, request counters, latency histograms, error alerts, queue-depth alerts, and a trace across at least three services.

**Material:** [Google SRE monitoring](https://sre.google/sre-book/monitoring-distributed-systems/) · [Prometheus/Grafana videos](https://www.youtube.com/results?search_query=Prometheus+Grafana+distributed+tracing+system+design).

### 24. Security

**Summary:** Authentication answers who the caller is. Authorization answers what the caller may do. Encryption protects data in transit and at rest. Threat modeling identifies assets, attackers, trust boundaries, and abuse cases.

**Minimum checklist:** TLS, input validation, secure secrets, least privilege, audit logs, token expiry, key rotation, rate limiting, dependency updates, and safe error messages.

**Material:** [OWASP API Security Top 10](https://owasp.org/API-Security/) · [Security in system design](https://www.youtube.com/results?search_query=system+design+API+security+authentication+authorization+OWASP).

### 25. Reliability, disaster recovery, RTO, and RPO

**Summary:** Reliability means the system performs correctly over time and recovers from failure. RTO is the maximum acceptable recovery time. RPO is the maximum acceptable data loss measured in time.

**Trade-off:** Multi-region redundancy improves recovery but increases cost, replication complexity, and consistency challenges. Backups are not enough unless restoration is tested.

**Material:** [AWS Well-Architected reliability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) · [Disaster recovery videos](https://www.youtube.com/results?search_query=RTO+RPO+disaster+recovery+system+design).

### 26. OOP and SOLID

**Summary:** Encapsulation protects invariants, abstraction hides implementation details, polymorphism allows interchangeable implementations, and SOLID principles help code remain changeable.

**Practical test:** If adding a new payment provider requires changing many unrelated classes, the design probably has poor abstraction or violates the Open/Closed Principle.

**Material:** [Refactoring Guru](https://refactoring.guru/design-patterns) · [OOP and SOLID videos](https://www.youtube.com/results?search_query=OOP+SOLID+principles+low+level+design+interview).

### 27. Design patterns

**Summary:** Factory centralizes object creation. Strategy swaps algorithms. Observer broadcasts changes. Builder constructs complex objects. Adapter converts incompatible interfaces. Decorator adds behavior without changing the wrapped class. Repository separates persistence from domain logic.

**Warning:** Patterns are tools, not requirements. Adding a pattern without a real variation or boundary increases complexity.

**Material:** [Design Patterns](https://refactoring.guru/design-patterns) · [LLD design pattern videos](https://www.youtube.com/results?search_query=low+level+design+design+patterns+Factory+Strategy+Observer+Decorator).

### 28. Concurrency and thread safety

**Summary:** Concurrency means multiple tasks overlap in execution. A race condition occurs when correctness depends on timing. A deadlock occurs when tasks wait forever for each other’s locks.

**Solutions:** Use immutable data, atomic operations, carefully scoped locks, idempotent commands, queues, and database constraints. Measure contention rather than adding locks everywhere.

**Watch:** [Concurrency and thread safety](https://www.youtube.com/results?search_query=low+level+design+concurrency+thread+safety+race+condition+deadlock).

### 29. UML and architecture diagrams

**Summary:** Component diagrams show system boundaries and dependencies. Sequence diagrams show time-ordered interactions. Class diagrams show LLD relationships. Deployment diagrams show runtime placement.

**Rule:** A diagram should answer a question. Do not draw every class when discussing HLD, and do not draw only boxes when the question requires object responsibilities.

**Material:** [PlantUML guide](https://plantuml.com/guide) · [UML system design videos](https://www.youtube.com/results?search_query=UML+class+sequence+diagram+low+level+design+interview).

### 30. Cost and trade-offs

**Summary:** Every architecture spends money and operational attention. Compare alternatives using latency, reliability, consistency, complexity, team ownership, data volume, and cost.

**Example:** A queue may reduce API latency and smooth traffic, but it adds broker cost, delayed processing, retries, monitoring, and eventual consistency.

**Material:** [AWS Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/the-pillars-of-the-framework.html) · [System design trade-off videos](https://www.youtube.com/results?search_query=system+design+tradeoffs+reliability+cost+latency+consistency).

## Readiness test

Use the companion file [system-design-questions.txt](./system-design-questions.txt). Score each answer from 0 to 4:

- 0: cannot explain it
- 1: definition only
- 2: definition plus example
- 3: applies it in a design and explains trade-offs
- 4: can design, implement, troubleshoot, and compare alternatives

For 100 questions, 300+ points indicates strong intermediate readiness. Also complete eight 45-minute designs. Each answer should contain requirements, estimates, APIs, data model, architecture, scaling, failure handling, security, observability, and trade-offs.

## Important distinction about answer videos

YouTube has walkthroughs for most canonical questions, but no single video reliably answers all 100 questions. The roadmap therefore links answer searches and trusted channels beside each topic. Watch a solution only after attempting the problem yourself; otherwise you may recognize the design without being able to produce it independently.

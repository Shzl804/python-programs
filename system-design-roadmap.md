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

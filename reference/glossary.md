# Glossary

## A

**API Gateway**
A server that acts as an API front-end, receiving API requests, enforcing throttling and security policies, passing requests to the back-end service, and then passing the response back to the requester. In microservices architectures, it serves as a single entry point for all client requests.

**Aggregate**
In Domain-Driven Design, a cluster of domain objects that can be treated as a single unit. An aggregate will have one of its component objects be the aggregate root, and any references from outside the aggregate should only go to the aggregate root.

**Anti-Corruption Layer (ACL)**
A layer that isolates a client's domain model from another system's domain model. It translates between the two models, preventing the client's model from being corrupted by the other system's design.

**Asynchronous Communication**
A communication pattern where the sender does not wait for a response from the receiver before continuing with other tasks. Common in microservices for loose coupling between services.

## B

**Bounded Context**
A central pattern in Domain-Driven Design that defines the boundaries within which a particular domain model is defined and applicable. In microservices, each service typically represents one bounded context.

**Bulkhead Pattern**
A resilience pattern that isolates elements of an application into pools so that if one fails, the others will continue to function. Named after the partitioned sections of a ship's hull.

**Backend for Frontend (BFF)**
An architectural pattern where separate backend services are created for different frontend applications or user experiences, allowing each frontend to have an API tailored to its specific needs.

**Backpressure**
A mechanism to handle situations where data is coming in faster than it can be processed, preventing system overload by controlling the flow of data.

## C

**Circuit Breaker**
A design pattern that prevents an application from repeatedly trying to execute an operation that's likely to fail, allowing it to continue without waiting for the fault to be fixed or wasting CPU cycles.

**Command Query Responsibility Segregation (CQRS)**
A pattern that separates read and update operations for a data store. CQRS can maximize performance, scalability, and security in microservices architectures.

**Consumer-Driven Contract Testing**
A testing approach where the consumer of a service defines the contract (expectations) for how the service should behave, and the provider verifies they can meet these expectations.

**Conway's Law**
The principle that organizations design systems that mirror their own communication structure. Formulated by Melvin Conway in 1967.

**Correlation ID**
A unique identifier that is passed through all services involved in processing a single request, enabling distributed tracing and debugging across service boundaries.

**Chaos Engineering**
The discipline of experimenting on a system to build confidence in the system's capability to withstand turbulent conditions in production.

## D

**Data Mesh**
An architectural paradigm that treats data as a product, with domain teams owning their data products and providing them to other teams through well-defined interfaces.

**Data Fabric**
A technology-centric approach that uses active metadata, AI/ML, and knowledge graphs to create a unified data access layer across distributed data sources.

**Dead Letter Queue (DLQ)**
A queue that stores messages that cannot be processed successfully after multiple retry attempts, preventing poison messages from blocking the processing of other messages.

**Distributed Monolith**
An anti-pattern where a system is deployed as separate services but maintains the coupling characteristics of a monolith, requiring coordinated deployments and shared databases.

**Domain-Driven Design (DDD)**
An approach to software development that centers the development on programming a domain model that has a rich understanding of the processes and rules of a domain.

**Distributed Tracing**
A method of tracking requests as they flow through multiple services in a distributed system, providing visibility into the entire request lifecycle.

## E

**Event Sourcing**
A pattern where state changes are stored as a sequence of events, allowing the system to reconstruct the current state by replaying these events.

**Event-Driven Architecture**
An architectural pattern where services communicate through the production and consumption of events, promoting loose coupling and scalability.

**Eventual Consistency**
A consistency model used in distributed computing that guarantees that, if no new updates are made to a given data item, eventually all accesses to that item will return the last updated value.

**External Configuration**
The practice of storing configuration parameters outside of the application code, allowing the same application to be deployed across different environments without code changes.

## F

**Fault Tolerance**
The ability of a system to continue operating properly in the event of the failure of some of its components.

**Function as a Service (FaaS)**
A cloud computing service that allows developers to run code in response to events without managing servers, often used for implementing microservices functionality.

## G

**GraphQL**
A query language and runtime for APIs that allows clients to request exactly the data they need, reducing over-fetching and under-fetching of data.

**gRPC**
A high-performance, open-source universal RPC framework that uses HTTP/2 for transport and Protocol Buffers as the interface description language.

## H

**Health Check**
An endpoint or mechanism that allows monitoring systems to determine if a service is running and healthy, essential for load balancing and service discovery.

**Hystrix**
A latency and fault tolerance library designed to isolate points of access to remote systems, services, and 3rd party libraries, stop cascading failure, and enable resilience.

## I

**Idempotency**
The property of certain operations whereby they can be applied multiple times without changing the result beyond the initial application.

**Infrastructure as Code (IaC)**
The practice of managing and provisioning computing infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.

**Inverse Conway Maneuver**
The practice of designing your team structure to match your desired architecture, leveraging Conway's Law to achieve the system design you want.

## J

**JSON Web Token (JWT)**
A compact, URL-safe means of representing claims to be transferred between two parties, commonly used for authentication and authorization in microservices.

## K

**VaquarKhan (Khan) Pattern™**
A context-aware framework for determining optimal microservice granularity, adapting to specific business context, team structure, and technical constraints.

**Kubernetes**
An open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.

## L

**Load Balancer**
A device or software that distributes network or application traffic across multiple servers to ensure no single server becomes overwhelmed.

**Loose Coupling**
A design principle where components have minimal dependencies on each other, allowing them to be modified independently without affecting other components.

## M

**Microservice**
A small, autonomous service that works together with other services to form a complete application. Each microservice is responsible for a specific business capability.

**Message Queue**
A form of asynchronous service-to-service communication used in serverless and microservices architectures, where messages are stored in a queue until they are processed.

**Mutual TLS (mTLS)**
A security protocol where both client and server authenticate each other using digital certificates, providing strong authentication for service-to-service communication.

**Monolith**
A software application that is designed as a single, indivisible unit, where all components are interconnected and interdependent.

## N

**Network Partition**
A failure scenario in distributed systems where network connectivity between nodes is lost, potentially causing consistency issues.

**Netflix OSS**
A collection of open-source tools developed by Netflix for building and operating microservices at scale, including Eureka, Hystrix, and Zuul.

## O

**Observability**
The ability to measure the internal states of a system by examining its outputs, typically through logs, metrics, and traces.

**Orchestration**
A pattern where a central coordinator manages the interactions between services to complete a business process.

**Outbox Pattern**
A pattern that ensures reliable publishing of events by storing them in the same database transaction as the business data, then publishing them asynchronously.

## P

**Poison Message**
A message that cannot be processed successfully and causes the consuming application to fail, potentially blocking the processing of other messages.

**Polyglot Persistence**
The practice of using different data storage technologies for different services based on their specific requirements.

**Property-Based Testing**
A testing approach where properties (invariants) of the system are defined and tested against randomly generated inputs to verify system correctness.

## Q

**Queue**
A data structure that follows the First-In-First-Out (FIFO) principle, commonly used for asynchronous communication between microservices.

## R

**Rate Limiting**
A technique for controlling the rate at which requests are made to a service, preventing overload and ensuring fair usage.

**Resilience**
The ability of a system to handle and recover from failures, maintaining acceptable levels of service.

**REST (Representational State Transfer)**
An architectural style for designing networked applications, commonly used for HTTP-based APIs in microservices.

**Retry Pattern**
A pattern that enables an application to handle transient failures by transparently retrying failed operations.

## S

**Saga Pattern**
A pattern for managing distributed transactions across multiple services by breaking them into a series of smaller, compensatable transactions.

**Service Discovery**
The process of automatically detecting and locating services within a network, essential for dynamic microservices environments.

**Service Mesh**
A dedicated infrastructure layer for handling service-to-service communication, providing features like load balancing, service discovery, and security.

**Sidecar Pattern**
A pattern where auxiliary functionality is deployed alongside the main application in a separate container or process.

**Single Responsibility Principle**
A principle stating that a class or service should have only one reason to change, promoting focused and maintainable code.

**Strangler Fig Pattern**
A pattern for gradually migrating from a legacy system by incrementally replacing functionality with new services.

## T

**Timeout**
A mechanism that prevents operations from running indefinitely by setting a maximum time limit for completion.

**Two-Phase Commit (2PC)**
A distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort the transaction.

## U

**Upstream/Downstream**
Terms describing the relationship between services in a request flow, where upstream services call downstream services.

## V

**Versioning**
The practice of managing changes to APIs and services over time while maintaining backward compatibility.

**Virtual Private Cloud (VPC)**
A logically isolated section of a cloud provider's infrastructure where you can launch resources in a virtual network.

## W

**WebAssembly (WASM)**
A binary instruction format that enables high-performance execution of code on web browsers and other environments, emerging as a potential deployment target for microservices.

## X

**X-as-a-Service**
A general term for various cloud computing service models (SaaS, PaaS, IaaS, FaaS, etc.) that provide specific capabilities as services.

## Y

**YAML (YAML Ain't Markup Language)**
A human-readable data serialization standard commonly used for configuration files in microservices deployments.

## Z

**Zero Trust**
A security model that requires verification for every person and device trying to access resources on a private network, regardless of whether they are sitting within or outside of the network perimeter.

**Zone**
A deployment target that represents a failure domain, such as an availability zone in cloud computing, used for distributing services to improve resilience.

---

## Usage Notes

This glossary provides definitions for terms as they are used in the context of microservices architecture. Some terms may have broader or different meanings in other contexts. For more detailed explanations and examples, please refer to the relevant chapters in this book.

Terms marked with ™ are proprietary concepts introduced in this book. All other terms represent industry-standard concepts and patterns.

---

*This glossary is maintained as a living document and may be updated as new terms and concepts emerge in the microservices field.*

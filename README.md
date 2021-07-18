
# Microservices Recipes- a free gitbook

#### Microservices are small, autonomous services that work together.

![Alt Text](https://cdn-images-1.medium.com/max/1600/1*os1hoijFv6Iupb11uKAKIA.gif)



## Table of Contents

* [Definition](#definition)
* [Why-Microservice](#Why-Microservice)
* [When-to-use-microservice-architecture](#When-to-use-microservice-architecture)
* [Pros-and-cons](#pros-and-cons)
* [Microservice-Design-Guidelines](#design-guidelines)
* [Certify-microservices-design](#Certify-microservices-design)
* [The-Scale-Cube](#The-Scale-Cube)
* [Microservices-vs-SOA](#Microservices-vs-SOA)
* [Microservices-vs-API](#Microservices-vs-API)
* [Microservice-vs-Miniservice](#Microservice-vs-Miniservice)
* [Microservice-vs-Nanoservices](#Microservice-vs-Nanoservices)
* [What-is-BoundedContext ](#What-is-BoundedContext )
* [Real-Life-Sucess-Stories ](#Real-Life-Sucess-Stories )
* [Orchestrate-microservices](#Orchestrate-microservices)
* [Theory ](#Theory )
* [Talks ](#Talks )
* [Tutorials ](#Tutorials )
* [Books ](#Books )
* [Sites ](#Sites )
* [Microservices-Quotes ](#Microservices-Quotes )
* [Resource-Naming ](#Resource-Naming )
* [Resource-Naming ](#Resource-Naming )
* [Microservices-Video ](#Microservices-Video )
* [Microservices-Patterns ](#Microservices-Patterns )
* [Code-example ](#Code-example )
* [Microservices-Anti-Patterns ](#Microservices-Anti-Patterns)
* [Article-Links ](#Article-Links )
* [The-Sins-of-Microservices](#The-Sins-of-Microservices )
* [Microservice-failure-stories](#Microservice-failure-stories )
* [API-Design-guidelines](#API-Design-guidelines)
* [REST-APIs-Design-guidelines](#REST-APIs-Design-guidelines)
* [Spring-Cloud-for-Microservices ](#Spring-Cloud-for-Microservices )
* [Kubernetes-for-Microservices ](#Kubernetes-for-Microservices )
* [Spring-Cloud-vs-Kubernetes  ](#Spring-Cloud-vs-Kubernetes )
* [REST-APIs-Design-guidelines](#REST-APIs-Design-guidelines)
* [RESTful URLs](#restful-urls)
* [HTTP Verbs](#http-verbs)
* [Responses](#responses)
* [Error handling](#error-handling)
* [Versions](#versions)
* [Record limits](#record-limits)
* [Request & Response Examples](#request--response-examples)
* [Mock Responses](#mock-responses)
* [API-Doc](#API-Doc)
* [Security](#Security)
* [Serialization](#Serialization)
* [Storage](#Storage)
* [Testing](#Testing)
* [Continuous-Integration-and-Continuous-Delivery](#Continuous-Integration-and-Continuous-Delivery)
* [Conway’s-Law ](#Conways-Law)


---------------------------------------------------------------------


## Definition

Microservice architecture, or simply microservices, is a distinctive method of developing software systems that tries to focus on building single-function modules with well-defined interfaces and operations. The trend has grown popular in recent years as Enterprises look to become more Agile and move towards a DevOps and continuous testing. Microservices can help create scalable, testable software that can be delivered weekly, not yearly.

![Alt Text](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/images/microservices-logical.svg)

Microservices architecture (courtesy: Cloud Application Architecture Guide and smartbear).

* Sam Newman : “Microservices are small, autonomous services that work together.”

* Frye:The idea with microservices is to focus on building individual services that do one thing and one thing well.

* Nic Grange, CTO at Retriever Communications: “Microservices are an approach to designing software systems that are made up of small independent services that each have a specific purpose.”

* Ali Hussain, CTO at Flux7: “Microservices are an approach to addressing a large or complex business problem using a set of smaller, simpler services that work together; a microservice runs its own unique process that contributes to an overarching business goal.”

* Dr. Ratinder Ahuja, Founder and CEO of ShieldX Networks: “Microservices are an approach to application development in which a large application is built as a suite of modular services. Each module supports a specific business goal and uses a simple, well-defined interface to communicate with other sets of services.”

* Dustin Horning, Solutions Engineer at Zesty.io: “Microservices are to software what factories are to manufacturing. Instead of having one person [or] machine build a whole car, each area is specialized in its task: This one hammers rivets, this one paints.” AND “Microservices is breaking down one large objective into its parts, and having those parts be accomplished independently.” (OK, that was two explanations, but we’ll let it slide.)

* Justin Bingham, CTO at Janeiro Digital: “Microservices are components of an application or broader ecosystem architected to operate independently – each responsible for a specific business or technical domain.”

* Michael Ducy, Director of Product Marketing at Chef: “It's breaking down the development and release of applications into smaller pieces of work.”

* Kong Yang, Head Geek at SolarWinds: “Microservices are a method of developing software applications which are made up of independently deployable, modular services. Each microservice runs a unique process and communicates through a well-defined, lightweight mechanism, such as a container, to serve a business goal.”

* Microservices allow an organization to reduce dependencies, develop faster, and scale.—Aviran Mordo

Microservices Definition by Lewis/Fowler:

* As a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API
* Services are built around business capabilities
* services are independently deployable and scalable
* Bare minimum of centralized management of these services
* Services may be written in different programming languages(polyglot development).
* Services should use separate data storage (polyglot persistence ).

“Microservices are important simply because they add unique value in a way of simplification of complexity in systems.  By breaking apart your system or application into many smaller parts, you show ways of reducing duplication, increasing cohesion and lowering your coupling between parts, thus making your overall system parts easier to understand, more scalable, and easier to change. The downside of a distributed system is that it is always more complex from a systems standpoint. The overhead of many small services to manage is another factor to consider. ”
― Lucas Krause,

The Microservices approach is about breaking your system ("pile of code") into many small services, each typically has its own:

* Clear business-related responsibility
* Running process
* Database
* Code version control (e.g. git) repository
* API (the protocol how other services / clients will contact the Microservice)
* UI


## Why-Microservice

* Microservice makes our system loosely coupled, i.e., if we need to update, repair, or replace a Microservice we, don't need to rebuild our entire application. Just swap out the part that needs it.
* To build each Microservice, can use different languages and tools. Microservices communicate with a well-defined interface.
* The communication should be stateless for scalability (copies of Microservice) and reliability (one copy fail other copy can serve). The most common methods for communication between Microservices are HTTP and messaging. Each Microservice should have its datastore.
* A small team capable work on design, web development, coding, database admin, and operations.

## When-to-use-microservice-architecture

Consider this architecture style for:

* Large applications that require a high release velocity.

* Complex applications that need to be highly scalable.

* Applications with rich domains or many subdomains.

* An organization that consists of small development teams.


## Pros-and-cons

### Advantages
Sam Newman in Building Microservices, enumerates the key benefits of Microservices as following:

#### Technology Heterogeneity
With a system composed of multiple, collaborating services, we can decide to use different technologies inside each one. This allows us to pick the right tool for each job, rather than having to select a more standardized, one-size-fits-all approach that often ends up being the lowest common denominator.

#### Resilience
A key concept in resilience engineering is the bulkhead. If one component of a system fails, but that failure doesn’t cascade, you can isolate the problem and the rest of the system can carry on working. Service boundaries become your obvious bulkheads. In a monolithic service, if the service fails, everything stops working. With a monolithic system, we can run on multiple machines to reduce our chance of failure, but with microservices, we can build systems that handle the total failure of services and degrade functionality accordingly.

#### Scaling
With a large, monolithic service, we have to scale everything together. One small part of our overall system is constrained in performance, but if that behavior is locked up in a giant monolithic application, we have to handle scaling everything as a piece. With smaller services, we can just scale those services that need scaling, allowing us to run other parts of the system on smaller, less powerful hardware.

#### Ease of Deployment
A one-line change to a million-line-long monolithic application requires the whole application to be deployed in order to release the change. That could be a large-impact, high-risk deployment. In practice, large-impact, high-risk deployments end up happening infrequently due to understandable fear.

With microservices, we can make a change to a single service and deploy it independently of the rest of the system. This allows us to get our code deployed faster. If a problem does occur, it can be isolated quickly to an individual service, making fast rollback easy to achieve.

#### Organizational Alignment
Microservices allow us to better align our architecture to our organization, helping us minimize the number of people working on any one codebase to hit the sweet spot of team size and productivity. We can also shift ownership of services between teams to try to keep people working on one service collocated.

#### Composability
One of the key promises of distributed systems and service-oriented architectures is that we open up opportunities for reuse of functionality. With microservices, we allow for our functionality to be consumed in different ways for different purposes. This can be especially important when we think about how our consumers use our software.

#### Optimizing for Replaceability
If you work at a medium-size or bigger organization, chances are you are aware of some big, nasty legacy system sitting in the corner. The one no one wants to touch. The one that is vital to how your company runs, but that happens to be written in some odd Fortran variant and runs only on hardware that reached end of life 25 years ago. Why hasn’t it been replaced? You know why: it’s too big and risky a job.

With our individual services being small in size, the cost to replace them with a better implementation, or even delete them altogether, is much easier to manage.

### Disadvantages

#### Team Communication Overhead -
Microservice architecture reduces the team management complexity, but it is not able to diminish the need of team communication. They need to make sure an update in one’s service is not breaking some other functionality. We can find this problem in monolith architecture applications too.

#### Non uniform application -
We can choose a different technology stack for a different component (polyglot). It leads to the problem of non uniform application design and architecture. It may can increase maintenance cost in the long run.

#### Dev Ops complexity -
We need to have a mature Dev Ops team to handle the complexity involved in maintaining Microservice based application. Due to several moving parts of the application, it becomes complex and requires a high level of expertise.
Increased Resource use - Initial investment to run these applications are high because all the independently running components need their own runtime containers with more memory and CPU.

#### Increase Network communication -
Independently running components interact with each other over a network. Such systems require reliable and fast network connections.
Marshalling and Un marshalling - When one component needs data from another component, the sender marshals the data in some standard from its internal representation, while the receiver un-marshalls data into its own representation before use. This definitely requires more processing compared to conventional application architecture.

#### Network Security -
Inter Service Communication needs to be secured to avoid any inter communication security breach. Due to several moving parts, these applications are more prone to security vulnerabilities.

#### Testing -
Testing of such application is definitely harder compared to a monolith application.

#### Production monitoring -
 Unavailability of the right tools are also an issue to be considered.

#### Log analysis -
Need log analysis tool for log analysis ,Splunk or ELK stack



![Alt Text](https://pbs.twimg.com/media/DEJ3V2xUwAIVS7i.jpg)
(Image courtesy:pivotal)

* Microservices - Not A Free Lunch! http://highscalability.com/blog/2014/4/8/microservices-not-a-free-lunch.html


* It is very difficult to maintain multiple Microservices as increased Complexity.

* It is extremely difficult to find good architects for creating Microservice architecture in right way.



## Design Guidelines

#### Architecture Principles

* Start with relatively broad service boundaries, to begin, refactoring to smaller ones (based on business requirements)
* [Single Responsibility Principle](https://codeburst.io/understanding-solid-principles-single-responsibility-b7c7ec0bf80)
* [domain-driven design](https://dzone.com/refcardz/getting-started-domain-driven?chapter=1)




#### Core patterns

* [Monolithic architecture from Chris Richardson](http://microservices.io/patterns/monolithic.html)
* [Microservices architecture from Chris Richardson](http://microservices.io/patterns/microservices.html)
* [API Gateway from Chris Richardson](http://microservices.io/patterns/apigateway.html)
* [Bounded Context from Martin Fowler](http://martinfowler.com/bliki/BoundedContext.html)
* [Circuit Breaker from Martin Fowler](http://martinfowler.com/bliki/CircuitBreaker.html)
* [Circuit Breaker ~ netflix](http://doc.akka.io/docs/akka/snapshot/common/circuitbreaker.html)

#### Deployment patterns

* [Multiple service instances per host](http://microservices.io/patterns/deployment/multiple-services-per-host.html)
* [Service instance per host](http://microservices.io/patterns/deployment/single-service-per-host.html)
* [Service instance per VM](http://microservices.io/patterns/deployment/service-per-vm.html)
* [Service instance per Container](http://microservices.io/patterns/deployment/service-per-container.html)

#### Service discovery

* [Client-side discovery from Chris Richardson](http://microservices.io/patterns/client-side-discovery.html)
* [Server-side discovery from Chris Richardson ](http://microservices.io/patterns/server-side-discovery.html)
* [Service registry pattern from Chris Richardson](http://microservices.io/patterns/service-registry.html)
* [Self registration pattern from Chris Richardson](http://microservices.io/patterns/self-registration.html)
* [3rd party registration pattern from Chris Richardson](http://microservices.io/patterns/3rd-party-registration.html)
* [Service discovery with consul & etcd](https://aws.amazon.com/blogs/compute/service-discovery-via-consul-with-amazon-ecs/)

#### Service Mesh

* [What Is a Service Mesh](https://www.nginx.com/blog/what-is-a-service-mesh/)
* [istio](https://istio.io/docs/concepts/what-is-istio/)
* [Service mesh vs api getway](https://medium.com/microservices-in-practice/service-mesh-vs-api-gateway-a6d814b9bf56)
* [Service Mesh With Istio on Kubernetes in 5 Steps](https://dzone.com/articles/service-mesh-with-istio-on-kubernetes-in-5-steps)


#### [Strategies and patterns for realizing the seven design guidelines applied to microservices (sei.cmu.edu)](https://www.sei.cmu.edu/education-outreach/courses/course.cfm?coursecode=P125)

#### Standardized service contract. Strategies include:
* [REST API design best practices](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
* [Apigee API gateway](https://apigee.com/about/cp/api-gateway)
* [WSO2 API Manager](https://wso2.com/api-manager/)    
* [contract-first design](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.435.2220&rep=rep1&type=pdf)     

#### Service loose coupling. Strategies include:
* [Service Facade pattern](https://www.ibm.com/support/knowledgecenter/pt-br/SSMKHH_9.0.0/com.ibm.etools.mft.pattern.sen.doc/sen/sf/overview.htm)  
* [Legacy Wrapper pattern](https://patterns.arcitura.com/soa-patterns/design_patterns/legacy_wrapper)
* [point-to-point, publish-subscribe and other messaging patterns](https://hackernoon.com/observer-vs-pub-sub-pattern-50d3b27f838c)  
* [event-driven architecture](https://microservices.io/patterns/data/event-driven-architecture.html)  

#### Service reusability. Strategies include:
* modeling for reuse  
* [Strangler Application pattern](https://www.martinfowler.com/bliki/StranglerApplication.html)   

#### Service autonomy. Strategies include:
* [Saga pattern](https://microservices.io/patterns/data/saga.html)
* [modeling services with DDD](https://www.thoughtworks.com/insights/blog/domain-driven-design-services-architecture)
* [Database per Microservice pattern](https://microservices.io/patterns/data/database-per-service.html)
* [Service Data Replication pattern](https://patterns.arcitura.com/soa-patterns/design_patterns/service_data_replication)
* [CQRS ](https://martinfowler.com/bliki/CQRS.html)
* [Event sourcing](https://microservices.io/patterns/data/event-sourcing.html)

#### Service statelessness. Strategies include:
* [Asynchronous processing](https://www.ibm.com/support/knowledgecenter/en/SSGMCP_4.2.0/com.ibm.cics.ts.intercommunication.doc/topics/dfht1ke.html)
* [State Messaging pattern](https://patterns.arcitura.com/soa-patterns/design_patterns/state_messaging)
* [Service Callback pattern](https://patterns.arcitura.com/soa-patterns/design_patterns/service_callback)


#### Service discoverability. Strategies include:
 * [service registry](https://microservices.io/patterns/service-registry.html)
 * [service governance](http://www.cs.cmu.edu/~ibm-soa/CMU-SOA-Day-Sachdeva-SOA-Governance.pdf)

#### Service deployability. Strategies include:
* [continuous delivery](https://martinfowler.com/bliki/ContinuousDelivery.html)
* [blue-green deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html)
* [externalized configuration](https://microservices.io/patterns/externalized-configuration.html)
* [containerization](https://cloud.google.com/containers/)
* [serverless architecture](https://martinfowler.com/articles/serverless.html)
* [monitoring and logging for microservices](https://dzone.com/articles/distributed-logging-architecture-for-microservices)


[![asciicast](https://i.vimeocdn.com/video/523960449.webp?mw=1000&mh=563&q=70)](https://vimeo.com/131632250)


### Microservice Design Patterns
* [Design patterns for microservices Article 1](https://azure.microsoft.com/en-us/blog/design-patterns-for-microservices/)
* [Design patterns for microservices Article 2](http://blog.arungupta.me/microservice-design-patterns/)
* [Design patterns for microservices Article 3](https://dzone.com/articles/design-patterns-for-microservices)
* [Design patterns for microservices Article 4](https://microservices.io/patterns/microservices.html)




Guidelines and examples for White House Web APIs, encouraging consistency, maintainability, and best practices across applications. White House APIs aim to balance a truly RESTful API interface with a positive developer experience (DX).

This document borrows heavily from:
* [Designing HTTP Interfaces and RESTful Web Services](https://www.youtube.com/watch?v=zEyg0TnieLg)
* [API Facade Pattern](http://apigee.com/about/resources/ebooks/api-fa%C3%A7ade-pattern), by Brian Mulloy, Apigee
* [Web API Design](http://pages.apigee.com/web-api-design-ebook.html), by Brian Mulloy, Apigee
* [Fielding's Dissertation on REST](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)
* [Cloud Design Patterns](https://docs.microsoft.com/en-us/azure/architecture/patterns/)

### Certify-microservices-design

After you identify the microservices in your application, validate your design against the following criteria:

* Each service has a single responsibility.
* There are no chatty calls between services. If splitting functionality into two services causes them to be overly chatty, it may be a symptom that these functions belong in the same service.
* Each service is small enough that it can be built by a small team working independently.
* There are no inter-dependencies that will require two or more services to be deployed in lock-step. It should always be possible to deploy a service without redeploying any other services.
* Services are not tightly coupled, and can evolve independently.
* Your service boundaries will not create problems with data consistency or integrity. Sometimes it's important to maintain data consistency by putting functionality into a single microservice. That said, consider whether you really need strong consistency. There are strategies for addressing eventual consistency in a distributed system, and the benefits of decomposing services often outweigh the challenges of managing eventual consistency.

- from docs.microsoft.com

### Can we reuse Microservice  ?

Reuse continues to be a principle of microservice design. However, the scope of reuse has been reduced to specific domains within the business. The effort of designing for this reuse, which in the early days of SOA included wasted efforts in designing enterprise-wide canonical models, was fruitless because it was too ambitious.

However, it must be noted that the canonical model in its restricted scope can be of benefit. In line with the reuse it facilitates, its scope has been reduced. With the ‘merit based reuse’ approach, an emerging model is preferred over a predetermined one. Teams can agree on communication models for deciding how microservices must be adapted for use outside the contexts in which they were designed.

If an existing microservice API does not suit your domain or ‘business group’, you might be better off building another microservice that does it.


-Alison Jarris


###  Know where you stand or going in future Architecture

![Alt Text](https://cdn-images-1.medium.com/max/2000/1*f5yQlyPApGNPfauFBe0pTA.png )

* Single purpose — each service should focus on one single purpose and do it well.
* Loose coupling — services know little about each other. A change to one service should not require changing the others. Communication between services should happen only through public service interfaces.
* High cohesion — each service encapsulates all related behaviors and data together. If we need to build a new feature, all the changes should be localized to just one single service.

- [From Xiao Ma article]( https://medium.engineering/microservice-architecture-at-medium-9c33805eb74f)


### The-Scale-Cube
Scale Cube, defined by Martin L. Abbott and Michael T. Fisher. This model explains how infinite scaling can be achieved by implementing a three-dimensional approach.

The Art of Scalability  book describes three dimension scalability model: the scale cube.  The microservice architecture is an application of Y-axis scaling on the scale cube.

    •	Horizontal Duplication and Cloning (X-Axis )
    •	Functional Decomposition and Segmentation - Microservices (Y-Axis)
    •	Horizontal Data Partitioning - Shards (Z-Axis)


![Alt Text](https://microservices.io/i/DecomposingApplications.021.jpg )

Scale Cube (Image courtesy:microservices.io)

  - https://microservices.io/articles/scalecube.html
 -  https://akfpartners.com/growth-blog/scale-cube/
 -  https://www.infoq.com/articles/microservices-intro
 -  https://medium.com/@cinish/microservices-architecture-5da90504f92a
 - https://github.com/vaquarkhan/awesome-scalability

###  Microservices-vs-SOA

![Alt Text](http://lh6.ggpht.com/-rMus2S1lWlY/VSbOJPqvxzI/AAAAAAAAAhI/7FZBTbZRLk8/MicroservicesVsSOA-SystemLayers.png?imgmax=800)

- https://dzone.com/articles/microservices-vs-soa-whats-the-difference
- http://www.soa4u.co.uk/2015/04/a-word-about-microservice-architectures.html

###  Microservices-vs-API

APIs are standardized wrappers that create an interface through which microservices can be packaged and surfaced. This makes APIs the logical enforcement point for key concerns of a microservices architecture such as security, governance, and reuse. Because APIs are able to house these concerns, they are considered a foundational component of a microservices architecture(mulesoft).                        
Microservices are design to use internally, while APIs are used to expose functionality to the outside world.

- https://www.youtube.com/watch?v=qGFRbOq4fmQ

### Microservice-vs-Miniservice

Miniservices have been called pragmatic microservices. You can get started with them faster and pick and choose the pieces that make sense for your team.

“[A miniservice is] like a group of microservices come together in a little pattern.”
— Ross Garrett

“Each microservice must handle its own data, miniservices may share data.”
— Arnaud Lauret

Don’t confuse architectural perfection with business value.”
— Ross Garrett


Leveraging the pieces of that practice that makes sense for me and getting most of the functionality benefits," says Ross Garrett.

- https://searchmicroservices.techtarget.com/feature/Miniservices-may-deliver-much-to-microservices-purists-chagrin
- https://thenewstack.io/miniservices-a-realistic-alternative-to-microservices/

### Microservice-vs-Nanoservices

Nanoservice is an antipattern where a service is too fine-grained. A nanoservice is a service whose overhead (communications, maintenance, and so on) outweighs its utility.


### What-is-BoundedContext

DDD deals with large models by dividing them into different Bounded Contexts and being explicit about their interrelationships.
Martin fowler

How big a Microservice should be is: it should have a well defined bounded context that will enable us to work without having to consider, or swap, between contexts.

#### How to identify bounded context  ?

- https://github.com/vaquarkhan/Domain-driven-design

# Real-Life-Sucess-Stories
- [ Companies about their experiences using microservices:](https://microservices.io/articles/whoisusingmicroservices.html)
- [How we build microservices at Karma](https://blog.yourkarma.com/building-microservices-at-karma)
- [How we ended up with microservices at SoundCloud](http://philcalcado.com/2015/09/08/how_we_ended_up_with_microservices.html)
- [Microservices: lessons from the frontline](https://www.thoughtworks.com/insights/blog/microservices-lessons-frontline)
- [Scaling microservices at Gilt with Scala, Docker and AWS](http://www.infoq.com/news/2015/04/scaling-microservices-gilt)
- [Walmart Successfully Revitalized its Failing Architecture with Microservices](https://www.youtube.com/watch?v=SPGCdziXlHU)
- [Spotify Builds User Experience with Microservices](https://www.youtube.com/watch?v=7LGPeBgNFuU)
- [Adopting Microservices at Netflix: Lessons for Architectural Design](https://www.nginx.com/blog/microservices-at-netflix-architectural-best-practices/)
- [One Call expand the transport network beyond popular ride-sharing services](https://www.sourcefuse.com/microservices-design-development-explained-case-study/)
- [Etsy Moved to an API-First Architecture:](https://www.infoq.com/news/2016/08/etsy-api-first-architecture)
- [Best Buy transformation.:](https://blog.runscope.com/posts/monolith-microservices-transforming-real-world-ecommerce-platform-using-strangler-pattern)
- [Cradlepoint:](https://cradlepoint.com/blog/matt-messinger/behind-code-series-how-we-moved-monolith-microservices)
- [virtusa:](https://www.virtusa.com/success-story/virtusa-modernizes-retirement-services-processing-leveraging-devops-and-microservices/)
- [Uber Engineering:] (https://eng.uber.com/building-tincup/)
- [Lessons From the Birth of Microservices at Google
:] (https://dzone.com/articles/lessons-from-the-birth-of-microservices-at-google)
- [Cloud Native Journey in Synchrony Financial:](https://content.pivotal.io/slides/cloud-native-journey-in-synchrony-financial)
- [Capital one Building Microservices on AWS using Serverless Framework :](https://www.youtube.com/watch?v=7mBo6pT09RM)


![Alt Text](http://szjug.github.io/files/20150917-big-data/big-data-dog-2.jpg)

---------------------------------------------------------------------------------


### Orchestrate vs Choreography


![Service orchestration](https://i.stack.imgur.com/hUbdsm.png)

The relationship between all the participating services are described by a single endpoint

![Service Choreography](https://i.stack.imgur.com/e186jm.png)

Service choreography is a global description of the participating services, which is defined by exchange of messages, rules of interaction and agreements between two or more endpoints. Choreography employs a decentralized approach for service composition.

andrei from stack


"We came across the decision to orchestrate our microservices by using a "god" like service that controls the business logic or a choreographed approach where the microservices basically pass messages, In microservice architecture choreography is preferred over orchestration."


### Orchestrate-microservices

* Conductor is an orchestration engine (Netflix orchestration framwork)
- https://netflix.github.io/conductor/

* Zeebe is a new open source orchestration engine for distributed microservices. It allows users to define orchestration flows visually using BPMN. Zeebe is horizontally scalable and fault tolerant so that you can reliably process all your transactions as they happen.

- https://zeebe.io/

#### If you create own orchestration Remember:

- You are an orchestrator, a coordinator of data and functions. You are not a transformer. Stay out of the business of messing with other people’s schema.

- Recommended ones include the Saga pattern, routing slips, and stateful workflows. Each pattern works with a certain level of complexity. Study up and match the right patterns to your orchestration.

- https://medium.com/capital-one-tech/microservices-when-to-react-vs-orchestrate-c6b18308a14c



---------------------------------------------------------------------------------



## Theory

![Alt Text](http://www.animatedimages.org/data/media/53/animated-book-image-0032.gif)

### Articles & Papers

- [AKF Scale Cube](http://akfpartners.com/techblog/2008/05/08/splitting-applications-or-services-for-scale/) - Model depicting the dimensions to scale a service.
- [Benchmark Requirements for Microservices Architecture Research](https://goo.gl/14ElnV) :small_orange_diamond:<sup>PDF</sup> - Set of requirements that may be useful in selecting a community-owned architecture benchmark to support repeatable microservices research.
- [Building Microservices? Here is What You Should Know](https://cloudncode.blog/2016/07/22/msa-getting-started/) - A practical overview, based on real-world experience, of what one would need to know in order to build Microservices.
- [CALM](http://db.cs.berkeley.edu/papers/cidr11-bloom.pdf) :small_orange_diamond:<sup>PDF</sup> - Consistency as logical monotonicity.
- [Canary Release](http://martinfowler.com/bliki/CanaryRelease.html) - Technique to reduce the risk of introducing a new software version in production by slowly rolling out the change to a small subset of users before rolling it out to the entire infrastructure and making it available to everybody.
- [CAP Theorem](http://blog.thislongrun.com/2015/03/the-cap-theorem-series.html) -  States that it is impossible for a distributed computer system to simultaneously provide all three of the following guarantees: Consistency, Availability and Partition tolerance.
- [Cloud Design Patterns](https://msdn.microsoft.com/en-us/library/dn600223.aspx) - Contains twenty-four design patterns that are useful in cloud-hosted applications. Includes: Circuit Breaker, Competing Consumers, CQRS, Event Sourcing, Gatekeeper, Cache-Aside, etc.
- [Microservice Architecture](http://martinfowler.com/articles/microservices.html) - Particular way of designing software applications as suites of independently deployable services.
- [Microservices and SOA](http://www.oracle.com/technetwork/issue-archive/2015/15-mar/o25architect-2458702.html) - Similarities, differences, and where we go from here.
- [Microservices – Please, don’t](http://basho.com/posts/technical/microservices-please-dont/) - Critical advice about some problems regarding a microservices approach.
- [Microservices RefCard](https://dzone.com/refcardz/getting-started-with-microservices) - Getting started with microservices.
- [Microservices Trade-Offs](http://martinfowler.com/articles/microservice-trade-offs.html) - Guide to ponder costs and benefits of the mircoservices architectural style.
- [Reactive Manifesto](http://www.reactivemanifesto.org/) - Reactive systems definition.
- [Reactive Streams](http://www.reactive-streams.org/) - Initiative to provide a standard for asynchronous stream processing with non-blocking back pressure.
- [ROCAS](http://resources.1060research.com/docs/2015/Resource-Oriented-Computing-Adaptive-Systems-ROCAS-1.2.pdf) :small_orange_diamond:<sup>PDF</sup> - Resource Oriented Computing for Adaptive Systems.
- [SECO](http://ceur-ws.org/Vol-746/IWSECO2011-6-DengYu.pdf) :small_orange_diamond:<sup>PDF</sup> - Understanding software ecosystems: a strategic modeling approach.
- [Service Discovery in a Microservice Architecture](https://www.nginx.com/blog/service-discovery-in-a-microservices-architecture/) - Overview of discovery and registration patterns.
- [Testing Strategies in a Microservice Architecture](http://martinfowler.com/articles/microservice-testing/) - Approaches for managing the additional testing complexity of multiple independently deployable components.
- [Your Server as a Function](http://monkey.org/~marius/funsrv.pdf) :small_orange_diamond:<sup>PDF</sup> - Describes three abstractions which combine to present a powerful programming model for building safe, modular, and efficient server software: Composable futures, services and filters.
- [A Journey into Microservices](https://sudo.hailoapp.com/services/2015/03/09/journey-into-a-microservice-world-part-1/)
- [Clean microservice architecture](http://blog.cleancoder.com/uncle-bob/2014/10/01/CleanMicroserviceArchitecture.html)
- [Failing at microservices](https://rclayton.silvrback.com/failing-at-microservices)
- [How to talk to your friends about microservices](https://blog.pivotal.io/labs/labs/how-to-talk-to-your-friends-about-microservices)
- [Monolith first](http://martinfowler.com/bliki/MonolithFirst.html)

-----

### Talks

- [Bla Bla Microservices Bla Bla](http://jonasboner.com/bla-bla-microservices-bla-bla/) - A talk at the O’Reilly Software Architecture Conference, April 2016.
- [Challenges in Implementing MicroServices](https://www.youtube.com/watch?v=yPf5MfOZPY0) - A presentation at GOTO 2015 by Fred George.
- [Microservices](https://www.youtube.com/watch?v=wgdBVIX9ifA) - A presentation at GOTO Berlin 2014 by Martin Fowler.

### Tutorials

- [Developing a RESTful Microservice in Python](http://www.skybert.net/python/developing-a-restful-micro-service-in-python/) - A story of how an aging Java project was replaced with a microservice built with Python and Flask.
- [Developing and Testing Microservices With Docker](http://mherman.org/blog/2017/04/18/developing-and-testing-microservices-with-docker) - An example of the processes involved in creating a simple Docker-packaged Node microservice.
- [Game On!](https://game-on.org/) - Microservices architecture explained in the context of an old-school text-based adventure game.
- [Microservices without the Servers](https://aws.amazon.com/blogs/compute/microservices-without-the-servers/) - Step by step demo-driven talk about serverless architecture.
- Microservices in C#: [Part 1](http://insidethecpu.com/2015/07/17/microservices-in-c-part-1-building-and-testing/), [Part 2](http://insidethecpu.com/2015/07/31/microservices-in-c-part-2-consistent-message-delivery/), [Part 3](http://insidethecpu.com/2015/08/14/microservices-in-c-part-3-queue-pool-sizing/), [Part 4](http://insidethecpu.com/2015/08/28/microservices-in-c-part-4-scaling-out/), [Part 5](http://insidethecpu.com/2015/09/11/microservices-in-c-part-5-autoscaling/).
- [Microservices with Python, RabbitMQ and Nameko](http://brunorocha.org/python/microservices-with-python-rabbitmq-and-nameko.html)
- [Reactive Microservices](https://github.com/theiterators/reactive-microservices) - Project showcasing different microservice communication styles using Scala, Akka, Play and other tools from Scala ecosystem.
- [Using Packer and Ansible to build immutable infrastructure](https://blog.codeship.com/packer-ansible/)

### Books

- [Building Microservices](https://www.nginx.com/wp-content/uploads/2015/01/Building_Microservices_Nginx.pdf) :small_orange_diamond:<sup>PDF</sup> - Building Microservices: Designing Fine-grained Systems. Sam Newman. Preview Edition.
- [Microservice Architecture: Aligning Principles, Practices, and Culture](http://shop.oreilly.com/product/0636920050308.do) - Practical advice for the strategy and design of Microservices.
- [Microservices in Action](https://www.manning.com/books/microservices-in-action) - A practical book about building and deploying microservice-based applications.
- [Microservice Patterns](https://www.manning.com/books/microservice-patterns) - Teaches how to build applications with the microservice architecture and how to refactor a monolithic application to a microservices.
- [Microservices from Theory to Practice](http://www.redbooks.ibm.com/abstracts/sg248275.html?Open) - Microservices from Theory to Practice: Creating Applications in IBM Bluemix Using the Microservices Approach. IBM Redbooks publication.
- [Migrating to Cloud Native Application Architectures](http://pivotal.io/platform/migrating-to-cloud-native-application-architectures-ebook) - This O’Reilly report defines the unique characteristics of cloud native application architectures such as microservices and twelve-factor applications.
- [Testing Microservices with Mountebank](https://www.manning.com/books/testing-microservices-with-mountebank) - Provides a testing strategy using mountebank for service virtualization, promoting independent releases of Microservices
- [The Art of Scalability](http://theartofscalability.com/) - The Art of Scalability: Scalable Web Architecture, Processes, and Organizations for the Modern Enterprise. Martin L. Abbott, Michael T. Fisher.
- [The New Stack eBook Series](http://thenewstack.io/ebookseries/) - A Comprehensive Overview of the Docker and Container Ecosystem.
  + Book 1: The Docker Container Ecosystem.
  + Book 2: Applications & Microservices with Docker & Containers.
  + Book 3: Automation & Orchestration with Docker & Containers.
  + Book 4: Network, Security & Storage with Docker & Containers.
  + Book 5: Monitoring & Management with Docker & Containers.
- [The Tao of Microservices](https://www.manning.com/books/the-tao-of-microservices) - Teaches the path to understanding how to apply microservices architecture with your own real-world projects.
* - [IBM Redbook](https://www.redbooks.ibm.com/redbooks/pdfs/sg248275.pdf) - IBM Red book
* [Antifragile: Things That Gain from Disorder](http://www.amazon.com/gp/product/0812979680)
* [The Black Swan](http://www.amazon.com/The-Black-Swan-Improbable-Robustness/dp/081297381X)
* [Implementing Domain-Driven Design](http://www.amazon.co.uk/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577)
* [Building Micro Services - Sam Newman](http://www.amazon.co.uk/Building-Microservices-Sam-Newman/dp/1491950358)
* [Building Micro Services - Sam Newman Downloadable preview edition](http://nginx.com/wp-content/uploads/2015/01/Building_Microservices_Nginx.pdf)
* [Antifragile Software - Russ Miles](https://leanpub.com/antifragilesoftware)
* [software-architecture-patterns from O`REILLY in English](http://www.oreilly.com/programming/free/files/software-architecture-patterns.pdf)
* [Production Ready Microservices - Susan J. Fowler](http://shop.oreilly.com/product/0636920053675.do)
* [Microservices in Production - Susan J. Fowler (free ebook)](http://www.oreilly.com/programming/free/microservices-in-production.csp)
* [Microservices with Docker, Flask, and React - Michael Herman](https://testdriven.io/)
* [Microservices on AWS](https://d1.awsstatic.com/whitepapers/microservices-on-aws.pdf)


### Sites

- [Microservices Resource Guide](http://martinfowler.com/microservices/) - Martin Fowler's choice of articles, videos, books, and podcasts that can teach you more about the microservices architectural style.
- [Microservice Patterns](http://microservices.io/) - Microservice architecture patterns and best practices.
- [Microservice Antipatterns and Pitfalls](https://www.oreilly.com/ideas/microservices-antipatterns-and-pitfalls) - Microservice mostly known antipatterns and pitfalls.
- [The 12-Factors App](http://12factor.net) - A methodology for building software-as-a-service applications.


### Microservices-Quotes
* [Building-microservices]( https://www.goodreads.com/work/quotes/41956437-building-microservices-designing-fine-grained-systems)
* [Microservices-patterns-and-applications]( https://www.goodreads.com/work/quotes/45004498-microservices-patterns-and-applications-designing-fine-grained-service)


### Resource-Naming
- https://www.restapitutorial.com/lessons/restfulresourcenaming.html




-----------------------------------------------------------------


### Microservices-Video

![Alt Text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQE2UGRK07Psnp-c3A0AscUl8dledtVbXpYe4l_Tx4YegL2e-fWrg)


No                  |    about     | url
------------------- | ------------ | -------------------
1| What are the Advantages of Microservices? - Sam Newman  |- https://www.youtube.com/watch?v=KV3j3MZTXgk
2| Design Microservice Architectures the Right Way   |- https://www.youtube.com/watch?v=j6ow-UemzBc
3| Mastering Chaos - A Netflix Guide to Microservices    |- https://www.youtube.com/watch?v=CZ3wIuvmHeM
4| API Academy Microservices Boot Camp @ CA World: Designing a Microservices Architecture     |-https://www.youtube.com/watch?v=iZNSPKxAd5w
5| Data Strategies for Microservice Architectures    |- https://www.youtube.com/watch?v=n_V8hBRoshY
6| Refactor your Java EE application using Microservices and Containers by Arun Gupta   |-https://www.youtube.com/watch?v=iJVW7v8O9BU
7| Principles Of Microservices by Sam Newman s    |-https://www.youtube.com/watch?v=PFQnNFe27kU
8| PGOTO 2016 • Appsec and Microservices • Sam Newman  | - https://www.youtube.com/watch?v=wlt7nCRWx_w
9| Avoiding Microservice Megadisasters - Jimmy Bogard   | - https://www.youtube.com/watch?v=gfh-VCTwMw8
10| 10 Tips for failing badly at Microservices by David Schmitz  | -  https://www.youtube.com/watch?v=X0tjziAQfNQ
11| Lessons from the Birth of Microservices at Google   | - https://www.youtube.com/watch?v=Fz1PoXqxAZc
12| Event Sourcing You are doing it wrong by David Schmitz    | - https://www.youtube.com/watch?v=GzrZworHpIk
13| The hardest part of microservices is your data     | - https://www.youtube.com/watch?v=MrV0DqTqpFU
14| Data Design and Modeling for Microservices      | - https://www.youtube.com/watch?v=KPtLbSEFe6c
15| The Art of Discovering Bounded Contexts by Nick Tune       | - https://www.youtube.com/watch?v=ez9GWESKG4I
16| The challenges of migrating 150+ microservices to Kubernetes -Sarah Wells (Financial Times)       | - https://www.youtube.com/watch?v=fgI3cOdv87I&feature=youtu.be
17| Revitalizing Aging Architectures with Microservices       | - https://www.youtube.com/watch?v=SPGCdziXlHU



### Microservices-Patterns


No                  |    about     | url
------------------- | ------------ | -------------------
1| Developing Microservices with Aggregates Chris Richardson |- https://www.infoq.com/presentations/aggregates-modular-microservices
2| Top 5+ Microservices Architecture and Design Best Practices Ajitesh Kumar  |- https://dzone.com/articles/top-5-microservices-architecture-and-design-best-p
3|Microservices: Patterns and Practices Panel C. Richardson, R. Shoup, L. Ryan, R. Tangirala, and R. Schloming participate in a discussion on microservices and the challenges faced at scale, the strategies to use and more. |-https://www.infoq.com/presentations/microservices-patterns-practices-panel
4 | Microservices Patterns Red Hat Videos  |- https://www.youtube.com/watch?v=_YzzxrSIQGw
5|7 Microservice Patterns Explained (Ivar Grimstad)  |- https://www.youtube.com/watch?v=4IFVBfLBl1Y
6|Three Microservice Patterns to Tear Down Your Monoliths  |- https://www.youtube.com/watch?v=84W9iY3CwdQ
7|14 Architectural patterns for microservice development  |- https://www.youtube.com/watch?v=yVZS1HZrlEw
8|Reducing Microservices Architecture Complexity with Istio and Kubernetes  |- https://www.youtube.com/watch?v=k42jqkjtYKY
9|Developing Microservices with Aggregates  |- https://www.infoq.com/presentations/aggregates-modular-microservices
10| The Seven Deadly Sins of Microservices by Daniel Bryant     | - https://www.youtube.com/watch?v=Jw6TYEb1Opw
11| Microservices Anti-Patterns   | - https://www.youtube.com/watch?v=I56HzTKvZKc


-------------------------------------------------------------------
 ## Code-example

![Alt Text](https://ih0.redbubble.net/image.475329521.8750/ra%2Clongsleeve%2Cx925%2C101010%3A01c5ca27c6%2Cfront-c%2C210%2C180%2C210%2C230-bg%2Cf8f8f8.lite-1.jpg)



No               |  url
------------------- | -------------
1        | - https://github.com/vaquarkhan/microservice-poc
2        | - https://github.com/vaquarkhan/robot-shop
3        | - https://github.com/vaquarkhan/awesome-microservices
4        |- https://github.com/vaquarkhan/microservice-docker-project
5        |- https://github.com/vaquarkhan/flowing-retail-microservice-kafka
6        |- https://github.com/vaquarkhan/spring-boot-microservices-series
7        |- https://github.com/vaquarkhan/A-curated-list-of-Microservice
8        |- https://github.com/vaquarkhan/sample-spring-microservices
9        |-  https://github.com/vaquarkhan/microservice-kafka
10        |-  https://github.com/vaquarkhan/oreilly-building-microservices-training
11        |-   https://github.com/vaquarkhan/micromono
12        |-  https://github.com/vaquarkhan/spring-cloud-microservice-example
13        |-   https://github.com/vaquarkhan/jwt-microservices-JavaRoadStorm2016
14        |-   https://github.com/vaquarkhan/micro
15        |-   https://github.com/vaquarkhan/microservices-centralized-configuration
16        |-   https://github.com/vaquarkhan/micro-company
17        |-   https://github.com/vaquarkhan/PiggyMetrics-microservice-poc
18        |-   https://github.com/vaquarkhan/spring-cloud-microservice
19        |-   https://github.com/vaquarkhan/CQRS-microservice-sampler
20        |-   https://github.com/vaquarkhan/Microservices-Deployment-Cookbook
21        |-   https://github.com/vaquarkhan/storyteller-microservices
22        |-   https://github.com/vaquarkhan/microservice-security
23        |-   https://github.com/vaquarkhan/microservices-demo
24        |-   https://github.com/vaquarkhan/spring-cloud-microservices-ELKStack
25        |-   https://github.com/vaquarkhan/event-stream-processing-microservices
26        |-   https://github.com/vaquarkhan/FraudDetection-Microservices-gemfire
27        |-   https://github.com/vaquarkhan/microservice-sampler
28        |-   https://github.com/vaquarkhan/microserviceApplication
29        |-   https://github.com/vaquarkhan/Microservices-With-Spring-Student-Files
30        |-   https://github.com/vaquarkhan/spring-boot-netflix-microservice-demo
31        |-   https://github.com/vaquarkhan/spring-netflix-oss-microservices
32        |-   https://github.com/vaquarkhan/rest-microservices
33        |-   https://github.com/vaquarkhan/cloud-native-microservice-strangler-example
34        |-   https://github.com/vaquarkhan/microservices-SpringCloud-netflix
35        |-   https://github.com/vaquarkhan/knowledge-driven-microservice
36        |-   https://github.com/vaquarkhan/event-driven-microservices-platform
37        |-   https://github.com/vaquarkhan/devnexus-microservice-sample
38        |-   https://github.com/vaquarkhan/microservices
39        |-   https://github.com/vaquarkhan/Spring-Microservices
40        |-   https://github.com/vaquarkhan/bootiful-microservices
41        |-   https://github.com/vaquarkhan/vk-microservices-with-spring-cloud
42        |-   https://github.com/vaquarkhan/cf-SpringBootTrader-microservice
43        |-   https://github.com/vaquarkhan/Refactor-monolith-to-microservices
44        |-   https://github.com/vaquarkhan/microservices-dashboard
45        |-   https://github.com/vaquarkhan/microservice-camel-in-action
46        |-   https://github.com/vaquarkhan/cloud-native-app-microservice-labs
47        |-   https://github.com/vaquarkhan/spring-boot-8-microservices
48        |-   https://github.com/vaquarkhan/building-microservices
49        |-   https://github.com/vaquarkhan/spring-doge-microservice
50        |-   https://github.com/vaquarkhan/microservice-service-registration-and-discovery
51        |-   https://github.com/ewolff/microservice
52        |-   https://github.com/semplify/Reactive-Microservice-Training
53        |-   https://gitlab.com/training-microservices-2018-06
54        |-   https://github.com/vaquarkhan/train-ticket
55        |-   https://github.com/cer/event-sourcing-examples
56        |-   https://github.com/finn-no/Docker-and-Microservices
57        |-   https://github.com/nielskrijger/auth-server
58        |-   https://developer.github.com/v3/repos/
59        |-   https://github.com/vaquarkhan/ftgo-application
60        |-   https://github.com/IBM/GameOn-Java-Microservices-on-Kubernetes

### Microservices-Anti-Patterns

![Alt Text](https://vignette.wikia.nocookie.net/fantendo/images/4/48/BUT_IT%27S_WRONG.gif/revision/latest?cb=20141204195436)


No                  |    about     | url
------------------- | ------------ | -------------------
1| Don’t Build a Distributed Monolith  |- https://www.microservices.com/talks/dont-build-a-distributed-monolith/
2| In this talk from the API360 Microservices Summit in New York, June 2016,  Vijay Alagarasan of Asurion explores lessons learned and anti-patterns to avoid when implementing microservices.   |-  https://www.apiacademy.co/resources/videos/api360-microservices-summit-microservices-anti-patterns
3|Microservices Anti-Patterns   |- https://vimeo.com/198927025
4|Microservices Anti-Patterns   |- https://vimeo.com/118020043
5|API360 Microservices Summit – Microservices Antipatterns – Vijay Alagarasan, Asurion   |-  https://www.youtube.com/watch?v=uTGIrzzmcv8
6|Stefan Tilkov - Microservices Patterns and Anti-patterns    |- https://www.youtube.com/watch?v=VaYmRe104HU
7|10 Tips for failing badly at Microservices by David Schmitz     |- https://www.youtube.com/watch?v=X0tjziAQfNQ
8|10 Tips for failing badly at Microservices by David Schmitz     |-https://www.oreilly.com/library/view/microservices-antipatterns-and/9781491963937/video255789.html



### Article-Links

No                  |    about     | url
------------------- | ------------ | -------------------
1| Twitter |- https://developer.twitter.com/en/docs
2| Facebook |- https://developer.twitter.com/en/docs
3| LinkedIn |- https://www.linkedin.com/developers#
4| Google |- https://developers.google.com/+/web/api/rest/latest/activities/list
8| Microservices in Practice - Key Architectural Concepts of an MSA  |- https://wso2.com/whitepapers/microservices-in-practice-key-architectural-concepts-of-an-msa/
9|Guidelines for Designing Microservices  |- https://medium.com/@WSO2/guidelines-for-designing-microservices-71ee1997776c
10| Microservices Resource Guide  |- https://www.martinfowler.com/microservices/
10| 5 guiding principles you should know before you design a microservice   |- https://opensource.com/article/18/4/guide-design-microservices
11| Pattern: Microservice Architecture  |- https://microservices.io/patterns/microservices.html
12| Scaling Uber from 1 to 100s of Services   |- https://www.microservices.com/talks/scaling-uber-from-1-to-100s-of-services/
13| tagged by: domain driven design    |- https://martinfowler.com/tags/domain%20driven%20design.html
14| DDD - The Bounded Context Explained   |- http://blog.sapiensworks.com/post/2012/04/17/DDD-The-Bounded-Context-Explained.aspx
15| MicroservicePrerequisites    |- https://martinfowler.com/bliki/MicroservicePrerequisites.html
16| DevOpsCulture     |- https://martinfowler.com/bliki/DevOpsCulture.html
17| What are Cloud-Native Applications?      |-  https://pivotal.io/cloud-native
18| JSONP     |-  https://stackoverflow.com/questions/2067472/what-is-jsonp-all-about
19| Microservices architecture style      |-  https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices
20| Microservices architecture       |-  https://samnewman.io/talks/principles-of-microservices/
21| Designing microservices: Identifying microservice boundaries  |-  https://docs.microsoft.com/en-us/azure/architecture/microservices/microservice-boundaries
22 | DDD Strategic Patterns: How to Define Bounded Contexts   |-  https://dzone.com/articles/ddd-strategic-patterns-how-to-define-bounded-conte
23| Microservices    |- https://martinfowler.com/articles/microservices.html
24| Daniel Jacobson on Ephemeral APIs and Continuous Innovation at Netflix     |- https://www.infoq.com/news/2015/11/daniel-jacobson-ephemeral-apis
25| Versioning       |- https://cloud.google.com/apis/design/versioning
26|Semantic Versioning 2.0.0      |-https://semver.org/
27| RESTful API Design. Best Practices in a Nutshell.   |- https://blog.philipphauer.de/restful-api-design-best-practices/
28| Rest API Tutorial |- https://restfulapi.net/resource-naming/
29| REST API Design - Resource Modeling |-https://www.thoughtworks.com/insights/blog/rest-api-design-resource-modeling
30| Improve time to market with microservices  |-https://www.ibm.com/cloud/garage/architectures/microservices?cm_sp=Blog-_-blogcta-_-ArchCenter
31|Digital Applications using a Microservice Architecture  |-https://github.com/ibm-cloud-architecture/refarch-cloudnative



## The-Sins-of-Microservices

No                  |    about     | url
------------------- | ------------ | -------------------
1| Seven Microservices Anti-patterns  |- https://www.infoq.com/articles/seven-uservices-antipatterns
2| Microservices Anti-patterns: It’s All About the People  |- https://opencredo.com/blogs/microservices-anti-patterns-its-all-about-the-people/
3| The 7 Deadly Sins of Microservices  |-  https://opencredo.com/blogs/7-deadly-sins-of-microservices/
4| Microservices? Please, Don't  |-  https://dzone.com/articles/microservices-please-dont
5| How Anti-Patterns Can Stifle Microservices Adoption in the Enterprise |-  https://blog.appdynamics.com/engineering/how-to-avoid-antipatterns-with-microservices/


### Microservice-failure-stories

A compiled list to public failure/horror stories related to microservice infrastructure.

TBD

-------------------------------------------------------------------------------------------------------------


## API-Design-guidelines

1. Build the API with consumers in mind--as a product in its own right.
    * Not for a specific UI.
    * Embrace flexibility / tunability of each endpoint (see #5, 6 & 7).
    * Eat your own dogfood, even if you have to mockup an example UI.


1. Use the Collection Metaphor.
    * Two URLs (endpoints) per resource:
        * The resource collection (e.g. /orders)
        * Individual resource within the collection (e.g. /orders/{orderId}).
    * Use plural forms (‘orders’ instead of ‘order’).
    * Alternate resource names with IDs as URL nodes (e.g. /orders/{orderId}/items/{itemId})
    * Keep URLs as short as possible. Preferably, no more-than three nodes per URL.

1. Use nouns as resource names (e.g. don’t use verbs in URLs).

1. Make resource representations meaningful.
    * “No Naked IDs!” No plain IDs embedded in responses. Use links and reference objects.
    * Design resource representations. Don’t simply represent database tables.
    * Merge representations. Don’t expose relationship tables as two IDs.

1. Support filtering, sorting, and pagination on collections.

1. Support link expansion of relationships. Allow clients to expand the data contained in the response by including additional representations instead of, or in addition to, links.

1. Support field projections on resources. Allow clients to reduce the number of fields that come back in the response.

1. Use the HTTP method names to mean something:
    * POST - create and other non-idempotent operations.
    * PUT - update.
    * GET - read a resource or collection.
    * DELETE - remove a resource or collection.

1. Use HTTP status codes to be meaningful.
    * 200 - Success.
    * 201 - Created. Returned on successful creation of a new resource. Include a 'Location' header with a link to the newly-created resource.
    * 400 - Bad request. Data issues such as invalid JSON, etc.
    * 404 - Not found. Resource not found on GET.
    * 409 - Conflict. Duplicate data or invalid data state would occur.

1. Use ISO 8601 timepoint formats for dates in representations.

1. Consider connectedness by utilizing a linking strategy. Some popular examples are:
    * [HAL](http://stateless.co/hal_specification.html)
    * [Siren](https://github.com/kevinswiber/siren)
    * [JSON-LD](http://json-ld.org/)
    * [Collection+JSON](http://amundsen.com/media-types/collection/)

1. Use [OAuth2](http://oauth.net/2/) to secure your API.
    * Use a Bearer token for authentication.
    * Require HTTPS / TLS / SSL to access your APIs. OAuth2 Bearer tokens demand it. Unencrypted communication over HTTP allows for simple eavesdroppping and impersonation.

1. Use Content-Type negotiation to describe incoming request payloads.

    For example, let's say you're doing ratings, including a thumbs-up/thumbs-down and five-star rating. You have one route to create a rating: **POST /ratings**

    How do you distinguish the incoming data to the service so it can determine which rating type it is: thumbs-up or five star?

    The temptation is to create one route for each rating type: **POST /ratings/five_star** and **POST /ratings/thumbs_up**

    However, by using Content-Type negotiation we can use our same **POST /ratings** route for both types. By setting the *Content-Type* header on the request to something like **Content-Type: application/vnd.company.rating.thumbsup** or **Content-Type: application/vnd.company.rating.fivestar** the server can determine how to process the incoming rating data.

1. Evolution over versioning. However, if versioning, use the Accept header instead of versioning in the URL.
    * Versioning via the URL signifies a 'platform' version and the entire platform must be versioned at the same time to enable the linking strategy.
    * Versioning via the Accept header is versioning the resource.
    * Additions to a JSON response do not require versioning. However, additions to a JSON request body that are 'required' are troublesome--and may require versioning.
    * Hypermedia linking and versioning is troublesome no matter what--minimize it.
    * Note that a version in the URL, while discouraged, can be used as a 'platform' version. It should appear as the first node in the path and not version individual endpoints differently (e.g. api.example.com/v1/...).

1. Consider Cache-ability. At a minimum, use the following response headers:
    * ETag - An arbitrary string for the version of a representation. Make sure to include the media type in the hash value, because that makes a different representation. (ex: ETag: "686897696a7c876b7e")
    * Date - Date and time the response was returned (in RFC1123 format). (ex: Date: Sun, 06 Nov 1994 08:49:37 GMT)
    * Cache-Control - The maximum number of seconds (max age) a response can be cached. However, if caching is not supported for the response, then no-cache is the value. (ex: Cache-Control: 360 or Cache-Control: no-cache)
    * Expires - If max age is given, contains the timestamp (in RFC1123 format) for when the response expires, which is the value of Date (e.g. now) plus max age. If caching is not supported for the response, this header is not present. (ex: Expires: Sun, 06 Nov 1994 08:49:37 GMT)
    * Pragma - When Cache-Control is 'no-cache' this header is also set to 'no-cache'. Otherwise, it is not present. (ex: Pragma: no-cache)
    * Last-Modified - The timestamp that the resource itself was modified last (in RFC1123 format). (ex: Last-Modified: Sun, 06 Nov 1994 08:49:37 GMT)

1. Ensure that your GET, PUT, and DELETE operations are all [idempotent](http://www.restapitutorial.com/lessons/idempotency.html).  There should be no adverse side affects from operations.


---------------------------------------------------------------------------

## REST-APIs-Design-guidelines


These guidelines aim to support a truly RESTful API. Here are a few exceptions:
* Put the version number of the API in the URL (see examples below). Don’t accept any requests that do not specify a version number.
* Allow users to request formats like JSON or XML like this:
    * http://example.gov/api/v1/magazines.json
    * http://example.gov/api/v1/magazines.xml

### RESTful URLs

#### General guidelines for RESTful URLs
* A URL identifies a resource.
* URLs should include nouns, not verbs.
* Use plural nouns only for consistency (no singular nouns).
* Use HTTP verbs (GET, POST, PUT, DELETE) to operate on the collections and elements.
* You shouldn’t need to go deeper than resource/identifier/resource.
* Put the version number at the base of your URL, for example http://example.com/v1/path/to/resource.
* URL v. header:
    * If it changes the logic you write to handle the response, put it in the URL.
    * If it doesn’t change the logic for each response, like OAuth info, put it in the header.
* Specify optional fields in a comma separated list.
* Formats should be in the form of api/v2/resource/{id}.json

#### Good URL examples
* List of magazines:
    * GET http://www.example.gov/api/v1/magazines.json
* Filtering is a query:
    * GET http://www.example.gov/api/v1/magazines.json?year=2011&sort=desc
    * GET http://www.example.gov/api/v1/magazines.json?topic=economy&year=2011
* A single magazine in JSON format:
    * GET http://www.example.gov/api/v1/magazines/1234.json
* All articles in (or belonging to) this magazine:
    * GET http://www.example.gov/api/v1/magazines/1234/articles.json
* All articles in this magazine in XML format:
    * GET http://example.gov/api/v1/magazines/1234/articles.xml
* Specify optional fields in a comma separated list:
    * GET http://www.example.gov/api/v1/magazines/1234.json?fields=title,subtitle,date
* Add a new article to a particular magazine:
    * POST http://example.gov/api/v1/magazines/1234/articles

#### Bad URL examples
* Non-plural noun:
    * http://www.example.gov/magazine
    * http://www.example.gov/magazine/1234
    * http://www.example.gov/publisher/magazine/1234
* Verb in URL:
    * http://www.example.gov/magazine/1234/create
* Filter outside of query string
    * http://www.example.gov/magazines/2011/desc

#### HTTP Verbs

HTTP verbs, or methods, should be used in compliance with their definitions under the [HTTP/1.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html) standard.
The action taken on the representation will be contextual to the media type being worked on and its current state. Here's an example of how HTTP verbs map to create, read, update, delete operations in a particular context:

| HTTP METHOD | POST            | GET       | PUT         | DELETE |
| ----------- | --------------- | --------- | ----------- | ------ |
| CRUD OP     | CREATE          | READ      | UPDATE      | DELETE |
| /dogs       | Create new dogs | List dogs | Bulk update | Delete all dogs |
| /dogs/1234  | Error           | Show Bo   | If exists, update Bo; If not, error | Delete Bo |

(Example from Web API Design, by Brian Mulloy, Apigee.)


#### Responses

* No values in keys
* No internal-specific names (e.g. "node" and "taxonomy term")
* Metadata should only contain direct properties of the response set, not properties of the members of the response set

#### Good examples

No values in keys:

    "tags": [
      {"id": "125", "name": "Environment"},
      {"id": "834", "name": "Water Quality"}
    ],


#### Bad examples

Values in keys:

    "tags": [
      {"125": "Environment"},
      {"834": "Water Quality"}
    ],


#### Error handling

Error responses should include a common HTTP status code, message for the developer, message for the end-user (when appropriate), internal error code (corresponding to some specific internally determined ID), links where developers can find more info. For example:

    {
      "status" : 400,
      "developerMessage" : "Verbose, plain language description of the problem. Provide developers
       suggestions about how to solve their problems here",
      "userMessage" : "This is a message that can be passed along to end-users, if needed.",
      "errorCode" : "444444",
      "moreInfo" : "http://www.example.gov/developer/path/to/help/for/444444,
       http://drupal.org/node/444444",
    }

Use three simple, common response codes indicating (1) success, (2) failure due to client-side problem, (3) failure due to server-side problem:
* 200 - OK
* 400 - Bad Request
* 500 - Internal Server Error


#### Versions

* Never release an API without a version number.
* Versions should be integers, not decimal numbers, prefixed with ‘v’. For example:
    * Good: v1, v2, v3
    * Bad: v-1.1, v1.2, 1.3
* Maintain APIs at least one version back.


#### Record limits

* If no limit is specified, return results with a default limit.
* To get records 51 through 75 do this:
    * http://example.gov/magazines?limit=25&offset=50
    * offset=50 means, ‘skip the first 50 records’
    * limit=25 means, ‘return a maximum of 25 records’

Information about record limits and total available count should also be included in the response. Example:

    {
        "metadata": {
            "resultset": {
                "count": 227,
                "offset": 25,
                "limit": 25
            }
        },
        "results": []
    }

### Request & Response Examples

#### API Resources

  - [GET /magazines](#get-magazines)
  - [GET /magazines/[id]](#get-magazinesid)
  - [POST /magazines/[id]/articles](#post-magazinesidarticles)

### GET /magazines

Example: http://example.gov/api/v1/magazines.json

Response body:

    {
        "metadata": {
            "resultset": {
                "count": 123,
                "offset": 0,
                "limit": 10
            }
        },
        "results": [
            {
                "id": "1234",
                "type": "magazine",
                "title": "Public Water Systems",
                "tags": [
                    {"id": "125", "name": "Environment"},
                    {"id": "834", "name": "Water Quality"}
                ],
                "created": "1231621302"
            },
            {
                "id": 2351,
                "type": "magazine",
                "title": "Public Schools",
                "tags": [
                    {"id": "125", "name": "Elementary"},
                    {"id": "834", "name": "Charter Schools"}
                ],
                "created": "126251302"
            }
            {
                "id": 2351,
                "type": "magazine",
                "title": "Public Schools",
                "tags": [
                    {"id": "125", "name": "Pre-school"},
                ],
                "created": "126251302"
            }
        ]
    }

#### GET /magazines/[id]

Example: http://example.gov/api/v1/magazines/[id].json

Response body:

    {
        "id": "1234",
        "type": "magazine",
        "title": "Public Water Systems",
        "tags": [
            {"id": "125", "name": "Environment"},
            {"id": "834", "name": "Water Quality"}
        ],
        "created": "1231621302"
    }



#### POST /magazines/[id]/articles

Example: Create – POST  http://example.gov/api/v1/magazines/[id]/articles

Request body:

    [
        {
            "title": "Raising Revenue",
            "author_first_name": "Jane",
            "author_last_name": "Smith",
            "author_email": "jane.smith@example.gov",
            "year": "2012",
            "month": "August",
            "day": "18",
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ante ut augue scelerisque ornare. Aliquam tempus rhoncus quam vel luctus. Sed scelerisque fermentum fringilla. Suspendisse tincidunt nisl a metus feugiat vitae vestibulum enim vulputate. Quisque vehicula dictum elit, vitae cursus libero auctor sed. Vestibulum fermentum elementum nunc. Proin aliquam erat in turpis vehicula sit amet tristique lorem blandit. Nam augue est, bibendum et ultrices non, interdum in est. Quisque gravida orci lobortis... "
        }
    ]

- https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm#sec_5_2_1_1

---------------------------------------------------------------------------------
### AWS Microservices

- https://www.linkedin.com/posts/sayten_1-hour-for-microservices-for-busy-professionals-ugcPost-6780519830018674688-rHnD/

-------------------------------------------------------------------------------
 ### Spring-Cloud-for-Microservices

   ![Alt Text](images/diagram-distributed-systems.svg)
   - https://spring.io/projects/spring-cloud

### Kubernetes-for-Microservices

TBD

### Spring-Cloud-vs-Kubernetes

![Alt Text](https://developers.redhat.com/blog/wp-content/uploads/2016/12/screen-shot-2016-12-06-at-10-32-19-768x310.png)



### Spring Cloud
Spring Cloud provides tools for developers to quickly build some of the common patterns in distributed systems such as configuration management, service discovery, circuit breakers, routing, etc. It is build on top of Netflix OSS libraries, written in Java, for Java developers.

### Strengths
* The unified programing model offered by the Spring Platform itself and rapid application creation abilities of Spring Boot give developers a great microservice development experience. For example, with few annotations, you can create a Config Server, and with few more annotations, you can get the client libraries to configure your services.

* There is a rich selection of libraries covering the majority of runtime concerns. Since all libraries are written in Java, it offers multiple features, greater control, and fine tuning options.

* The different Spring Cloud libraries are well-integrated with one another. For example, a Feign client will also use Hystrix for Circuit Breaking, and Ribbon for load balancing requests. Everything is annotation driven, making it easy to develop for Java developers.

### Weaknesses
* One of the major advantages of the Spring Cloud is also its drawback — it is limited to Java only. A strong motivation for the MSA is the ability to interchange technology stacks, libraries, and even languages, when required. That is not possible with Spring Cloud. If you want to consume Spring Cloud/Netflix OSS infrastructure services, such as configuration management, service discovery, or load balancing, the solution is not elegant. The Netflix Prana project implements the sidecar pattern to expose Java-based client libraries over HTTP to make it possible for applications written in non-JVM languages to exist in the NetflixOSS ecosystem, but it is not very elegant.

* There is too much responsibility for Java developers to care about and for Java applications to handle. Each microservice needs to run various clients for configuration retrieval, service discovery, and load balancing. It is easy to set those up, but that doesn't hide the buildtime and runtime dependencies to the environment. For example, developers can create a Config Server with @EnableConfigServer, but that is only the happy path. Every time developers want to run a single microservice, they need to have the Config Server up and running. For a controlled environment, developers have to think about making the Config Server highly available, and since it can be backed by Git or Svn, they need a shared file system for it. Similarly, for service discovery, developers need to start a Eureka server first. For a controlled environment, they need to cluster it with multiple instances on each AZ, etc. It feels like as a Java developers have to build and manage a non-trivial microservices platform in addition to implementing all the functional services.

* Spring Cloud alone has a shorter scope in the microservices journey, and developers will also need to consider automated deployments, scheduling, resource management, process isolation, self-healing, build pipelines, etc. for a complete microservices experience. For this point, I think it is not fair to compare Spring Cloud alone to Kubernetes, and a more fair comparison would be between Spring Cloud + Cloud Foundry (or Docker Swarm) and Kubernetes. But that also means that for a complete end-to-end microservices experience, Spring Cloud must be supplemented with an application platform like Kubernetes itself.


### Kubernetes
Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications. It is polyglot and provides primitives for provisioning, running, scaling and managing distributed systems.

### Strengths
* Kubernetes is a polyglot and language agnostic container management platform that is capable of running both cloud-native and traditional containerized applications. The services it provides, such as configuration management, service discovery, load balancing, metrics collection, and log aggregation, are consumable by a variety of languages. This allows having one platform in the organization that can be used by multiple teams (including Java developers using Spring) and serve multiple purposes: application development, testing environments, build environments (to run source control system, build server, artifact repositories), etc.

* When compared to Spring Cloud, Kubernetes addresses a wider set of MSA concerns. In addition to providing runtime services, Kubernetes also lets you provision environments, set resource constraints, RBAC, manage application lifecycle, enable autoscaling and self-healing (behaving almost like an antifragile platform).

* Kubernetes technology is based on Google's 15 years of R&D and experience of managing containers. In addition, with close to 1000 committers, it is one of the most active Open Source communities on Github.

### Weaknesses
* Kubernetes is polyglot and, as such, its services and primitives are generic and not optimized for different platforms such as Spring Cloud for JVM. For example, configurations are passed to applications as environment variables or a mounted file system. It doesn't have the fancy configuration updating capabilities offered by Spring Cloud Config.

* Kubernetes is not a developer-focused platform. It is intended to be used by DevOps-minded IT personnel. As such, Java developers need to learn some new concepts and be open to learning new ways of solving problems. Despite it being super easy to start a developer instance of Kubernetes using MiniKube, there is a significant operation overhead to install a highly available Kubernetes cluster manually.

* Kubernetes is still a relatively new platform (2 years old), and it is still actively developed and growing. Therefore there are many new features added with every release that may be difficult to keep up with. The good news is that this has been envisaged, and the API is extensible and backward compatible.

 [From Bilgin Ibryam Article  ](https://dzone.com/articles/deploying-microservices-spring-cloud-vs-kubernetes)
* [Spring Cloud for Microservices Compared to Kubernetes](https://developers.redhat.com/blog/2016/12/09/spring-cloud-for-microservices-compared-to-kubernetes/)

---------------------------------------------------------------------------------


* [Microservicios 2.0: Spring Cloud Netflix vs Kubernetes & Istio
](https://www.paradigmadigital.com/dev/microservicios-2-0-spring-cloud-netflix-vs-kubernetes-istio/)

---------------------------------------------------------------------------------

### Mock Responses
It is suggested that each resource accept a 'mock' parameter on the testing server. Passing this parameter should return a mock data response (bypassing the backend).

Implementing this feature early in development ensures that the API will exhibit consistent behavior, supporting a test driven development methodology.

Note: If the mock parameter is included in a request to the production environment, an error should be raised.

---------------------------------------------------------------------------------

### API-Doc


- [Aglio](https://github.com/danielgtaylor/aglio) - API Blueprint renderer with theme support that outputs static HTML.
- [API Blueprint](https://apiblueprint.org/) - Tools for your whole API lifecycle. Use it to discuss your API with others. Generate documentation automatically. Or a test suite. Or even some code.
- [Apidoc](https://github.com/mbryzek/apidoc) - Beautiful documentation for REST services.
- [RAML](http://raml.org/) - RESTful API Modeling Language, a simple and succinct way of describing practically-RESTful APIs.
- [Slate](https://github.com/tripit/slate) - Beautiful static documentation for your API.
- [Spring REST Docs](http://projects.spring.io/spring-restdocs/) - Document RESTful services by combining hand-written documentation with auto-generated snippets produced with Spring MVC Test.
- [Swagger](http://swagger.io/) - A simple yet powerful representation of your RESTful API.

---------------------------------------------------------------------------------

### Security

- [Crtauth](https://github.com/spotify/crtauth) - A public key backed client/server authentication system.
- [Dex](https://github.com/coreos/dex) - Opinionated auth/directory service with pluggable connectors. OpenID Connect provider and third-party OAuth 2.0 delegation.
- [JWT](http://jwt.io/) - JSON Web Tokens are an open, industry standard RFC 7519 method for representing claims securely between two parties.
- [Keycloak](https://github.com/keycloak/keycloak) - Full-featured and extensible auth service. OpenID Connect provider and third-party OAuth 2.0 delegation.
- [Light OAuth2](https://github.com/networknt/light-oauth2) - A fast, lightweight and cloud native OAuth 2.0 authorization microservices based on light-java.
- [Login With](https://github.com/lipp/login-with) - Stateless login-with microservice for Google, FB, Github, and more.
- [OAuth](http://oauth.net/2/) - Provides specific authorization flows for web applications, desktop applications, mobile phones, and living room devices. Many implementations.
- [OpenID Connect](http://openid.net/developers/libraries/) - Libraries, products, and tools implementing current OpenID specifications and related specs.
- [OSIAM](https://github.com/osiam/osiam) - Open source identity and access management implementing OAuth 2.0 and SCIMv2.
- [SCIM](http://www.simplecloud.info/) - System for Cross-domain Identity Management.
- [Vault](https://www.vaultproject.io/) - Secures, stores, and tightly controls access to tokens, passwords, certificates, API keys, and other secrets in modern computing.
- [RFC5246](https://tools.ietf.org/html/rfc5246) - The Transport Layer Security (TLS) Protocol Version 1.2.
- [RFC6066](https://tools.ietf.org/html/rfc6066) - TLS Extensions.
- [RFC6347](https://tools.ietf.org/html/rfc6347) - Datagram Transport Layer Security Version 1.2.
- [RFC6749](https://tools.ietf.org/html/rfc6749) - The OAuth 2.0 authorization framework.
- [RFC7515](https://tools.ietf.org/html/rfc7515) - JSON Web Signature (JWS) represents content secured with digital signatures or Message Authentication Codes (MACs) using JSON-based data structures.
- [RFC7519](https://tools.ietf.org/html/rfc7519) - JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties.
- [RFC7642](https://tools.ietf.org/html/rfc7642) - SCIM: Definitions, overview, concepts, and requirements.
- [RFC7643](https://tools.ietf.org/html/rfc7643) - SCIM: Core Schema, provides a platform-neutral schema and extension model for representing users and groups.
- [RFC7644](https://tools.ietf.org/html/rfc7644) - SCIM: Protocol, an application-level, REST protocol for provisioning and managing identity data on the web.
- [OIDCONN](http://openid.net/connect/) - OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol. It allows clients to verify the identity of the end-user based on the authentication performed by an Authorization Server, as well as to obtain basic profile information about the end-user in an interoperable and REST-like manner.

---------------------------------------------------------------------------------

### Serialization

- [Avro](https://avro.apache.org/) - Apache data serialization system providing rich data structures in a compact, fast, binary data format.
- [BooPickle](https://github.com/ochrons/boopickle) - Binary serialization library for efficient network communication. For Scala and Scala.js
- [Cap’n Proto](https://capnproto.org/) - Insanely fast data interchange format and capability-based RPC system.
- [CBOR](http://cbor.io/) - Implementations of the CBOR standard (RFC 7049) in many languages.
- [Cereal](http://uscilab.github.io/cereal/) - C++11 library for serialization.
- [Cheshire](https://github.com/dakrone/cheshire) - Clojure JSON and JSON SMILE encoding/decoding.
- [Etch](http://etch.apache.org/) - Cross-platform, language and transport-independent framework for building and consuming network services.
- [Fastjson](https://github.com/alibaba/fastjson) - Fast JSON Processor.
- [Ffjson](https://github.com/pquerna/ffjson) - Faster JSON serialization for Go.
- [FST](https://github.com/RuedigerMoeller/fast-serialization) - Fast java serialization drop in-replacemen.
- [Jackson](https://github.com/FasterXML/jackson) -  A multi-purpose Java library for processing JSON data format.
- [Jackson Afterburner](https://github.com/FasterXML/jackson-module-afterburner) - Jackson module that uses bytecode generation to further speed up data binding (+30-40% throughput for serialization, deserialization).
- [Kryo](https://github.com/EsotericSoftware/kryo) - Java serialization and cloning: fast, efficient, automatic.
- [MessagePack](http://msgpack.org/) - Efficient binary serialization format.
- [Protostuff](https://github.com/protostuff/protostuff) - A serialization library with built-in support for forward-backward compatibility (schema evolution) and validation.
- [SBinary](https://github.com/harrah/sbinary) - Library for describing binary formats for Scala types.
- [Thrift](http://thrift.apache.org/) - The Apache Thrift software framework, for scalable cross-language services development.

---------------------------------------------------------------------------------

### Storage

- [Apache Hive](https://hive.apache.org/) - Data warehouse infrastructure built on top of Hadoop.
- [Apache Cassandra](http://cassandra.apache.org) - Column-oriented and providing high availability with no single point of failure.
- [Apache HBase](http://hbase.apache.org) - Hadoop database for big data.
- [Aerospike ![c]](http://www.aerospike.com/) - High performance NoSQL database delivering speed at scale.
- [ArangoDB](https://www.arangodb.com/) - A distributed free and open source database with a flexible data model for documents, graphs, and key-values.
- [AtlasDB](https://github.com/palantir/atlasdb) - Transactional layer on top of a key value store.
- [ClickHouse](https://clickhouse.yandex/) - Column-oriented database management system that allows generating analytical data reports in real time.
- [CockroachDB ![c]](https://www.cockroachlabs.com/product/cockroachdb-core/) - A cloud-native SQL database modelled after Google Spanner.
- [Couchbase](http://www.couchbase.com/) - A distributed database engineered for performance, scalability, and simplified administration.
- [Crate ![c]](https://crate.io/) - Scalable SQL database with the NoSQL goodies.
- [Datomic](http://www.datomic.com/) - Fully transactional, cloud-ready, distributed database.
- [Druid](http://druid.io/) - Fast column-oriented distributed data store.
- [Elasticsearch](https://www.elastic.co/products/elasticsearch) - Open source distributed, scalable, and highly available search server.
- [Elliptics](http://reverbrain.com/elliptics/) - Fault tolerant distributed key/value storage.
- [Geode](http://geode.incubator.apache.org/) - Open source, distributed, in-memory database for scale-out applications.
- [Infinispan](http://infinispan.org/) - Highly concurrent key/value datastore used for caching.
- [InfluxDB](https://github.com/influxdata/influxdb) - Scalable datastore for metrics, events, and real-time analytics.
- [Manta](https://www.joyent.com/manta) - Highly scalable, distributed object storage service with integrated compute.
- [MemSQL ![c]](http://www.memsql.com/) - High-performance, in-memory database that combines the horizontal scalability of distributed systems with the familiarity of SQL.
- [OpenTSDB](http://opentsdb.net) - Scalable and distributed time series database written on top of Apache HBase.
- [Parquet](https://parquet.apache.org/) - Columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language.
- [Reborn](https://github.com/reborndb/reborn) - Distributed database fully compatible with redis protocol.
- [RethinkDB](http://rethinkdb.com/) - Open source, scalable database that makes building realtime apps easier.
- [Secure Scuttlebutt](https://github.com/ssbc/docs) - P2P database of message-feeds.
- [Tachyon](http://tachyon-project.org/) - Memory-centric distributed storage system, enabling reliable data sharing at memory-speed across cluster frameworks.
- [Voldemort](https://github.com/voldemort/voldemort) - Open source clone of Amazon DynamoDB
- [VoltDB ![c]](https://www.voltdb.com/) - In-Memory ACID compliant distributed database.

---------------------------------------------------------------------------------

### Testing

- [Goreplay](https://github.com/buger/goreplay) - A tool for capturing and replaying live HTTP traffic into a test environment.
- [Mitmproxy](https://mitmproxy.org/) - An interactive console program that allows traffic flows to be intercepted, inspected, modified and replayed.
- [Mountebank](http://www.mbtest.org/) - Cross-platform, multi-protocol test doubles over the wire.
- [Spring Cloud Contract](https://cloud.spring.io/spring-cloud-contract/) - TDD to the level of software architecture.
- [VCR](https://github.com/vcr/vcr) - Record your test suite's HTTP interactions and replay them during future test runs for fast, deterministic, accurate tests. See the list of ports for implementations in other languages.
- [Wilma](https://github.com/epam/Wilma) - Combined HTTP/HTTPS service stub and transparent proxy solution.
- [WireMock](http://wiremock.org/) - Flexible library for stubbing and mocking web services. Unlike general purpose mocking tools it works by creating an actual HTTP server that your code under test can connect to as it would a real web service.

---------------------------------------------------------------------------------

### Continuous-Integration-and-Continuous-Delivery


- [Awesome CI/CD DevOps](https://github.com/ciandcd/awesome-ciandcd) - A curated list of awesome tools for continuous integration, continuous delivery and DevOps.

---------------------------------------------------------------------------------

### Conways-Law

“Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.” — Melvin Conway (1967).


Conway's Law asserts that organizations are constrained to produce application designs which are copies of their communication structures. This often leads to unintended friction points.

The 'Inverse Conway Maneuver' recommends evolving your team and organizational structure to promote your desired architecture. Ideally your technology architecture will display isomorphism with your business architecture.

“Microservice,” :- “Microservice we are following mostly the domain-driven approach, the idea is to have a cross-functional team.”

* [Create smaller, multi-functional teams that are no bigger than what two pizzas can feed](https://www.bizjournals.com/bizjournals/how-to/human-resources/2016/11/jeff-bezos-two-pizza-rule-for-building-productive.html)
--------------------------------------------------

![Alt Text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjz5RYcuKTPMnf09nLpjxciGuQeAP58RH8IkIIsSomeqqrPHs2)


Inspired by the [coming soon...]().

---------------------------------------------------------------------------------
<object data="https://www.redbooks.ibm.com/redbooks/pdfs/sg248357.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://www.redbooks.ibm.com/redbooks/pdfs/sg248357.pdf">
        <p>This browser does not support PDFs. Please download the Microservice IBM Redbooks PDF to view it: <a href="https://www.redbooks.ibm.com/redbooks/pdfs/sg248357.pdf">Download PDF</a>.</p>
    </embed>




------------------------------------------------------------------------------------------------------

![Alt Text](http://bestanimations.com/Animals/Birds/Doves/animated-dove-gif-5.gif)


### Note :

- Draft version.
- You are welcome to contribute and participate in the building of the one page index for microservice. If you fail to find your name in the attribution, plz raise an issue on GitHub . If the claim is valid will add attribution to the content.      

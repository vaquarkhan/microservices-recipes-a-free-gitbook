
# Microservices Recipes: The  Architect's Field Guide
#### "The goal of architecture is not to decompose software; it is to compose value. Sometimes, the most scalable microservice is the one you delete." — Vaquar Khan

We have entered the Post-Microservices Era. The challenge is no longer how to split a monolith, but how to govern a sprawling mesh without succumbing to the Microservice Singularity.

This field guide moves beyond "Hello World" tutorials. It introduces The Khan Pattern™ (Adaptive Granularity)—a physics-based protocol for measuring Cognitive Load vs. Kinetic Friction. It provides the blueprints required to build systems that are secure by design, resilient by default, and mathematically justified.

![Alt Text](https://cdn-images-1.medium.com/max/1600/1*os1hoijFv6Iupb11uKAKIA.gif)



## Preface: The Architect’s Mandate
"If you are working in an organization that places lots of restrictions on how developers can do their work, then microservices may not be for you." — Sam Newman

The transition from monolithic architectures to microservices is not merely a change in deployment strategy; it is a fundamental reorganization of data governance, inter-process communication, and organizational sociology.

While the industry has coalesced around high-level definitions—"small, autonomous services that work together"—the practical reality of implementing them at scale is fraught with profound complexity. "Microservices" has become a loaded term, often conflated with specific technologies like Kubernetes or Docker, rather than being understood as an architectural style focused on the logical decomposition of complex systems.

## The Illusion of Order

In a monolith, order is enforced by the compiler. If you try to access a private class from a different module, the build fails. In a distributed system, the compiler is gone. Order must be maintained by consensus, governance, and resilience patterns.

This field guide is designed for the Senior Architect. It moves beyond rudimentary definitions to explore the nuanced trade-offs involved in distributed systems—the "hard parts" where no perfect solution exists, only compromises.

It synthesizes deep technical research, industry best practices, and specific cloud-native implementations—primarily within the Amazon Web Services (AWS) ecosystem—to provide a blueprint for building scalable, resilient, and secure distributed systems.

## The Gardener of Ecosystems

The era of the "Ivory Tower" architect—who hands down static UML diagrams to developers—is over. In a distributed world, the system evolves too fast for static blueprints.

The modern architect acts not as a dictator of blueprints but as a gardener of ecosystems. You cannot force a plant to grow, but you can create the environment (infrastructure), provide the nutrients (tooling), and trim the weeds (technical debt) to allow independent teams to thrive without descending into chaos.

We visualize this shift in responsibility below:

<img width="1234" height="175" alt="image" src="https://github.com/user-attachments/assets/0eb562b0-b0b5-48ec-9750-cfd9e623b02f" />

## How to Use This Field Guide

This book is structured not as a linear narrative, but as a collection of Strategic Patterns and Tactical Recipes.

- The Sociotechnical Substrate: We begin by accepting Conway's Law as a physical constraint, not a suggestion.
- The Physics of Scale: We introduce the Khan Granularity Protocol™, a method to measure the "Kinetic Friction" of your architecture to decide when to split a service.
- The Implementation: We dive into code-level patterns (Sagas, Outboxes, Circuit Breakers) necessary to survive the hostility of the network.

Welcome to the post-microservices era. It is time to stop splitting and start governing.

-------------------------------

# Part I: The Sociotechnical Substrate
Focus: Aligning organization and architecture to prevent the "Distributed Monolith."

## Chapter 1: The Definition Wars & The Reality of SOA

History is written by the victors, but in software architecture, it is often rewritten by marketing departments. To build a robust distributed system in the 2020s, we must first strip away the veneer of hype that covers the term "Microservices" and confront its lineage.

We are not building something entirely new; we are attempting Service-Oriented Architecture (SOA) without the tragic mistakes of the past. The Senior Architect must understand why SOA failed in the mid-2000s to avoid repeating those failures with Kubernetes today.

This chapter explores the "Definition Wars"—the semantic battles that define our trade—and provides a forensic tool to help you determine the true boundaries of your system, ignoring the lines drawn on the whiteboard in favor of the lines drawn in the commit history.

### 1.1 SOA vs. Microservices: "Service Orientation Done Right"

In the early 2000s, SOA promised a revolution. It promised that large enterprises could break down their silos, reuse logic across departments, and achieve unprecedented agility. It failed for a significant portion of the industry.

Why? Because it prioritized technical reuse over domain autonomy.

#### 1.1.1 The Fallacy of the Enterprise Service Bus (ESB)
The primary artifact of the SOA era was the Enterprise Service Bus (ESB). Organizations spent millions on proprietary middleware (Tibco, BizTalk, IBM Websphere) to centralize logic, routing, and transformation. The prevailing wisdom was: "Put the intelligence in the pipes so the endpoints can remain simple."

This led to the Enterprise Monolith—a distributed system where all business rules, routing logic, and data transformations lived in a centralized "God Component" managed by a specialized middleware team.

The Bottleneck: If the Checkout team wanted to change a data format, they had to file a ticket with the ESB team and wait six weeks for a WSDL update.

The Coupling: The ESB became the single point of failure and the single point of coupling.

#### 1.1.2 The Microservices Inversion
Microservices flip this paradigm entirely. As Martin Fowler and James Lewis famously articulated, microservices are characterized by "Smart endpoints and dumb pipes."

   
In a microservices architecture, the network (the pipe) should do nothing but transport packets. It should be HTTP, gRPC, or a simple message broker. The intelligence—the routing decisions, the business rules, the data mapping—must reside within the service itself.

The distinction is best visualized by the flow of governance and logic:

<img width="1273" height="375" alt="image" src="https://github.com/user-attachments/assets/2cd8f2be-8f55-4d55-961a-ee3ff299b332" />


#### 1.1.3 The Architect's Decision Matrix

The Senior Architect must differentiate between these styles to prevent "accidental SOA."

##### Feature	Classic SOA (The Anti-Pattern)	Microservices (The Goal) - Table 

Communication	Smart Pipes: The ESB handles routing, versioning, and logic.	Dumb Pipes: HTTP/gRPC transport only. Logic is in the code.
Data Governance	Shared Database: Often, services read from a single massive schema.	Database per Service: Strict encapsulation. Access via API only.
Primary Goal	Reuse: "Don't write the same code twice."	Replaceability: "Ability to rewrite a component easily."
Coupling	High: Coupled via the ESB and shared schema.	Low: Coupled only by Bounded Context APIs.
Team Structure	Horizontal: UI Team, DB Team, Middleware Team.	Vertical: Stream-aligned teams owning the full stack.

##### The Mandate: Do not build a microservices architecture that relies on a "Service Mesh" to handle heavy business logic. If your Istio or Envoy configuration contains complex routing rules based on business payload data, you have just reinvented the ESB.

## 1.2 The "Micro" Trap: Defining Boundaries by Replaceability

A pervasive anti-pattern in the industry is defining "Micro" by lines of code (e.g., "A service should be no more than 500 lines"). This is a metric of vanity, not utility. It leads to Nanoservices—components so fine-grained that the network latency overhead outweighs the computational value.   

A service is "Micro" if it is independently replaceable.

### 1.2.1 The Two-Week Rewrite Rule

A robust heuristic for the Senior Architect is the Two-Week Rewrite Rule:

A microservice should be small enough that a standard "Two-Pizza Team" (6-8 engineers) could rewrite it from scratch in two weeks without disrupting the rest of the system.

   

If a service is so large that you are afraid to touch it, it is a monolith. If it is so small that it does nothing but forward a request to another service, it is a Nanoservice.

#### 1.2.2 Granularity vs. Cognitive Load

The size of a service should be dictated by the Cognitive Load it imposes on the team. The Khan Granularity Protocol™ (detailed in the Addendum) suggests we optimize for the "Goldilocks Zone" where the team can hold the entire domain model in their working memory.

Low Cognitive Load: The team understands the code completely. They can deploy on Friday afternoon with confidence.

High Cognitive Load: The team needs "archaeologists" to understand the code. Deployments require "War Rooms" and manager approval.

We can visualize the relationship between Granularity and Overhead:

<img width="1254" height="314" alt="image" src="https://github.com/user-attachments/assets/9aca3b54-a250-466f-9644-064aea872bf6" />

    
Zone of Monolith: Complexity comes from code entanglement and slow build times.

Zone of Nanoservices: Complexity comes from network orchestration, serialization costs, and "Distributed Spaghetti."

Zone of Bounded Contexts: The ideal state where service boundaries align with business boundaries (e.g., "Payments," "Search").

## 1.3 The Reality of the Distributed Monolith

Most organizations attempting microservices end up building a Distributed Monolith. This is the worst of all worlds. It is a system deployed as separate artifacts but retaining the tight coupling of a monolith. It incurs the performance penalties of distributed systems (latency, serialization, network failure) without yielding the benefits (independent deployability).

### 1.3.1 Symptoms of a Distributed Monolith

Lock-Step Deployments: If Service A cannot be deployed without simultaneously upgrading Service B and Service C, they are not microservices. They are a single application torn apart by the network.

The Integration Database: Multiple services reading and writing to the same tables. If Service A changes a column name and Service B breaks, you have failed at encapsulation.

Chatty Interfaces: A single frontend request triggers a cascade of 50 synchronous internal calls. This destroys availability. If each of the 50 calls has a 99.9% success rate, the aggregate success rate is:

    
    $$0.999^{50} \approx 95\%$$

You have architected a system that fails 5% of the time by default.


## Recipe 1.1: Analyzing Git Commit History to Identify Boundaries

Problem: You are tasked with migrating a legacy monolith to microservices. How do you know where to draw the lines? Solution: Do not rely on static analysis (who calls whom). Rely on Temporal Coupling (who changes with whom).

Static analysis tools (like SonarQube) tell you about compile-time dependencies. They cannot see logical dependencies. However, the Git history tells the truth about behavioral dependencies. If OrderController.java and InventoryService.java are modified in the same Git commit 85% of the time, they are highly coupled. Splitting them would create a distributed transaction nightmare.

This recipe provides a forensic tool to generate a Coupling Matrix from your repository.

Prerequisites
Python 3.x

Git installed on the command line

Libraries: pandas, matplotlib, seaborn

##### Step 1: Extract the Raw Data
Run this command in the root of your monolith's repository. It extracts the history of file changes for every commit.

Bash
# Extract commit hash, date, author, and file stats

    git log --all --numstat --date=short --pretty=format:'--%h--%ad--%aN' --no-renames > git_log.txt


##### Step 2: The Analysis Script (coupling_forensics.py)

This script parses the log and calculates the Jaccard Similarity coefficient for every pair of files.

Python
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from itertools import combinations
    import sys
    import os

    def parse_git_log(filepath):
        """
        Parses the git log into a DataFrame of Commit Hash -> File Path
        """
        commits =
        current_commit = None
    
        if not os.path.exists(filepath):
            print(f"Error: File {filepath} not found. Run the git log command first.")
            sys.exit(1)

        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                if line.startswith('--'):
                    # New commit detected
                    parts = line.strip().split('--')
                    current_commit = parts[1] # Store Hash
                elif line.strip() and current_commit:
                    # File change detected (numstat format: added deleted filename)
                    parts = line.split()
                    if len(parts) >= 3:
                        # Reconstruct filename (handles spaces in paths)
                        filename = " ".join(parts[2:])
                        # Filter for source code only (customize extensions as needed)
                        if filename.endswith(('.java', '.go', '.ts', '.cs', '.py', '.js')):
                            commits.append({'commit': current_commit, 'file': filename})
    
        print(f"Parsed {len(commits)} file modifications.")
        return pd.DataFrame(commits)

    def calculate_coupling(df, min_co_changes=5):
        """
        Calculates Jaccard Similarity for file pairs.
        Formula: (Intersection / Union)
        """
        # Group files by commit to see what changed together
        commit_groups = df.groupby('commit')['file'].apply(list)
    
        pair_counts = {}
        file_counts = df['file'].value_counts()
    
        print("Calculating coupling matrix (this may take a moment)...")
    
        for files in commit_groups:
            # We need at least 2 files to form a pair
            if len(files) < 2: continue
        
            # Sort to ensure (A, B) is treated same as (B, A)
            sorted_files = sorted(set(files)) # set() removes duplicates in same commit
        
            for f1, f2 in combinations(sorted_files, 2):
                pair_counts[(f1, f2)] = pair_counts.get((f1, f2), 0) + 1
            
        results =
        for (f1, f2), intersection in pair_counts.items():
            if intersection < min_co_changes: continue # Ignore noise
        
            # Jaccard Index calculation
            union = file_counts[f1] + file_counts[f2] - intersection
            score = intersection / union
        
            results.append({
                'File A': f1, 
                'File B': f2, 
                'Co-Change Count': intersection, 
                'Coupling Score': round(score, 3)
            })
        
        return pd.DataFrame(results).sort_values(by='Coupling Score', ascending=False)

    if __name__ == "__main__":
        print("--- Microservices Forensics: Coupling Analysis ---")
        log_file = 'git_log.txt'
    
        df_commits = parse_git_log(log_file)
        if df_commits.empty:
            print("No commits found. Check your git_log.txt generation.")
            sys.exit()
        
        df_coupling = calculate_coupling(df_commits)
    
        print("\nTop 10 High Temporal Coupling Candidates:")
        print(df_coupling.head(10).to_markdown(index=False))
    
        # Save for review
        df_coupling.to_csv('coupling_report.csv', index=False)
        print("\nFull report saved to 'coupling_report.csv'.")


    
### 1.3.2 Interpreting the Forensics

The output will reveal the hidden structure of your application.

 File A	File B	Co-Change Count	Coupling Score (0-1)
 
    src/cart/CartService.java	src/pricing/PricingService.java	45	0.85
    src/order/OrderController.java	src/utils/DateFormatter.java	12	0.15

The "Red Zone" (Score > 0.7): These files change together constantly.

Diagnosis: They are temporally coupled.

Action: Do not separate them. If you place CartService and PricingService in different microservices, every time you change Pricing, you will break Cart. Keep them in the same Bounded Context.

The "Green Zone" (Score < 0.2): These files rarely affect each other.

Diagnosis: Low coupling.

Action: These are excellent candidates for separation. Splitting them carries low risk of "distributed monolith" behavior.

Architectural Insight: Often, this analysis reveals "God Classes" or "Utils" packages that couple unrelated domains. For example, if a Constants.java file has a coupling score of 0.3 with everything, it is a dependency magnet. The correct refactoring is to duplicate the constants into their specific domains (De-DRYing) before attempting to split the services.

## 1.4 Summary: The Geometry of Choice

The Senior Architect does not blindly "adopt microservices." They manipulate the geometry of the system based on the immediate constraint. Scaling the Y-axis (Functional Decomposition) is the most expensive operation in software engineering. Use the Coupling Matrix to ensure you are cutting along the joints, not sawing through the bone.

----------------------------------------------------

# Chapter 2: The Distributed Monolith and Anti-Patterns – An Expanded Field Guide

## 2.1 The Phenomenology of the Distributed Monolith

The transition from monolithic architectures to microservices is frequently eulogized in executive summaries as a panacea for the stagnation of legacy systems. The promise is seductive: rapid deployment cycles, independent scaling of components, and the freedom to adopt polyglot technology stacks that best fit the problem at hand. However, the chasm between the theoretical microservices architecture—characterized by bounded contexts and loose coupling—and the deployed reality is often filled with the wreckage of failed transformations. The most pervasive and pernicious of these failures is the "Distributed Monolith."

A Distributed Monolith is a system that consists of multiple services deployed in separate containers or servers but which lacks the defining characteristic of a true microservice architecture: loose coupling. In this pathological state, the system incurs all the inherent complexities of a distributed system—network latency, serialization costs, partial failures, and distributed tracing challenges—without reaping any of the benefits of agility or independence.1 It is, in essence, the worst of possible worlds: the rigidity of a monolith combined with the unreliability of a network.2

The emergence of the distributed monolith is rarely an intentional design choice; rather, it is an emergent property of organizational entropy and a misunderstanding of the physics of distributed computing. It occurs when teams decompose applications based on technical layers (e.g., separating the UI, logic, and data access layers into different services) rather than business domains. This results in a system where every business function requires a synchronous conversation between multiple services, re-creating the tight coupling of the monolith over a much slower and less reliable transport mechanism.3

### 2.1.1 The Mathematical Inevitability of Failure
The fundamental error in creating a Distributed Monolith is the violation of the fallacies of distributed computing, specifically regarding reliability and latency. When a monolithic application is sliced along technical layers rather than business domains, the resulting services must communicate incessantly to perform even the simplest unit of work.

Consider a synchronous call chain where Service A calls Service B, which calls Service C. If each service has a Service Level Objective (SLO) of 99.9% availability, the composite availability of the chain is the product of the individual availabilities. In a "chatty" distributed monolith, a single user request—such as "Checkout"—might trigger 50 synchronous internal calls to validate inventory, check credit limits, calculate tax, and update loyalty points. The mathematical availability drops precipitously.

The formula for system availability ($A_{system}$) in a synchronous chain is the product of the availability of each component ($A_{service}$) raised to the power of the number of dependencies ($n$):

     $$A_{system} = A_{service}^n$$
     
If we assume a standard cloud availability of 99.9% for each service, a chain of 50 calls results in:

     $$A_{system} = 0.999^{50} \approx 95.1\%$$
     
While 95% might sound acceptable in some contexts, it implies that one in twenty requests will fail purely due to the architecture, even if the code is bug-free. However, the reality is often grimmer. If the individual service availability is merely 99% (a common reality for non-optimized internal services or during deployment windows), the aggregate availability collapses to catastrophic levels:

    $$A_{system} = 0.99^{50} \approx 60.5\%$$

This mathematical reality explains why distributed monoliths are plagued by "ghost outages"—periods where the system is technically "up" (no single service is fully down/red on the dashboard), but user transactions fail due to timeouts and transient network glitches cascading through tight coupling chains.1 The latency tail is equally punitive; the 99th percentile latency of the composite service becomes the sum of the 99th percentile latencies of all downstream calls, ensuring that the system is only as fast as its slowest component.

### 2.1.2 A Taxonomy of Coupling

To diagnose a distributed monolith, the Architect must look beyond the deployment diagram and analyze the nature of the coupling. Coupling is not a binary state; it exists on a spectrum. Meilir Page-Jones’s concept of Connascence provides a rigorous vocabulary for this analysis, allowing us to categorize the severity of the dependency between services. In a distributed monolith, we often observe high degrees of static and dynamic connascence that bind services together as effectively as if they were compiled into a single binary.

#### Connascence of Identity (Spatial Coupling)

This occurs when Service A must know the exact network location (IP/Port) of Service B to function. While Service Discovery tools like Consul, Eureka, or AWS Cloud Map mitigate the hard-coding of IPs, the dependency on B’s immediate availability remains. If Service B moves or goes down, Service A fails. In a true microservice architecture, this is mitigated by asynchronous messaging where Service A pushes a message to a broker, indifferent to the location or even the existence of Service B.4

#### Connascence of Meaning (Semantic Coupling)

Service A and Service B share a specific, implicit understanding of a data value. For example, both services might understand that a status integer of 5 means "Shipped." If the "Shipping" service changes this interpretation to "Delivered" or introduces a new status 6, the "Order" service breaks or corrupts data. This is rampant in systems that share a database (The Integration Database Anti-Pattern), where the schema acts as a rigid, shared public API that cannot be evolved without cross-team coordination.1

#### Connascence of Timing (Temporal Coupling)

This is the most damaging form of coupling in distributed systems. Service A requires Service B to process a request right now to complete its own transaction. This precludes asynchronous processing and creates backpressure vulnerability. If Service B slows down, Service A’s thread pool fills up, and the failure cascades upstream. Temporal coupling transforms independent services into a single, fragile failure domain.
Connascence of Algorithm

This occurs when multiple services must agree on a specific algorithm to process data. A classic example is a shared hashing algorithm for checksums or a specific business rule for calculating tax that is duplicated across the "Cart," "Checkout," and "Invoice" services. If the tax law changes, every service must be updated and deployed simultaneously to avoid data inconsistency.

### 2.1.3 The "Common" Library Trap

A subtle but pervasive vector for the distributed monolith is the "Common" shared library. In monolithic development, the principle of DRY (Don't Repeat Yourself) is paramount. Developers are trained to extract shared logic (DTOs, utilities, domain objects) into a shared JAR, Gem, or NPM package.

In a microservices architecture, however, the indiscriminate use of shared libraries creates Binary Coupling. If the "Billing" service and the "Shipping" service both depend on common-lib-v1.0.jar, and the "Billing" team needs a change in the Customer object that resides in common-lib, the library must be updated to v1.1. Now, the "Shipping" team must also rebuild, retest, and redeploy their service to avoid classpath conflicts or serialization errors, even if they had no need for the change.1

This forces Lock-Step Deployment, where teams lose the ability to release independently. The shared library becomes a "God Class" that every team touches, leading to merge conflicts and coordination meetings.
Architect’s Heuristic: In microservices, prefer duplication over coupling. It is better to have two slightly different copies of a Customer class—one tailored for Billing (containing credit card tokens) and one for Shipping (containing address details)—than to tie the release cycles of two disparate teams together via a shared binary. DRY applies within a microservice boundary, not across them.

## 2.2 The Sociotechnical Origins: Conway’s Law Revisited

To understand why intelligent, well-intentioned engineering teams build distributed monoliths, we must look beyond technology to the sociotechnical mirroring mechanisms identified by Melvin Conway. The architecture of a system is rarely purely the result of technical decisions; it is a reflection of the communication structures of the organization that built it.

### 2.2.1 The Homomorphism of Design

In his seminal 1968 paper, "How Do Committees Invent?", Melvin Conway posited that "organizations which design systems (in the broad sense used here) are constrained to produce designs which are copies of the communication structures of these organizations".5 This observation, now known as Conway's Law, asserts that the interface structure of a software system will necessarily show a congruence—specifically a homomorphism—with the social structure of the organization that produced it.5

#### Conway observed a specific mechanism for this mirroring:

"The realization by the initial designers that the system will be large... make[s] irresistible the temptation to assign too many people to a design effort. Application of the conventional wisdom of management to a large design organization causes its communication structure to disintegrate." 5

When a monolithic organization—characterized by siloed functional departments like a "DBA Team," a "Backend Team," and a "Frontend Team"—attempts to build microservices, the communication costs dictate the architecture. The Backend team talks mostly to themselves, and occasionally to the DBAs. Consequently, they produce a single, monolithic "Backend Service" that connects to a single "Database." If they attempt to split it, they inevitably produce a layered distributed architecture that mirrors their silos:

- A "Data Service" (mirroring the DBA team).
- A "Business Logic Service" (mirroring the Backend team).
- A "BFF (Backend for Frontend) Service" (mirroring the Frontend team).

This structure is not a microservices architecture; it is a breakdown of the monolith into network-separated tiers. The teams must still coordinate on every feature release, necessitating high-bandwidth communication that the architecture was supposed to eliminate. The technical boundaries have become rigid because the social boundaries are rigid.

### 2.2.2 The Inverse Conway Maneuver

Recognizing this causality allows Architects to employ the Inverse Conway Maneuver (ICM). Originating from ThoughtWorks (Jonhy Leroy and Matt Simons, 2010), this strategy dictates that to achieve a specific technical architecture—such as decoupled, independently deployable microservices—one must first reshape the organizational structure to match it.9

The ICM transforms Conway’s Law from a descriptive observation into a normative design tool. Instead of fighting the organization to build the software, we design the organization to force the software into the desired shape.

#### Implementation Guide for the Architect:

Identify Bounded Contexts: Use Domain-Driven Design (DDD) to identify business domains (e.g., "Order Fulfillment," "Customer Acquisition") rather than technical layers.
Form Stream-Aligned Teams: Create cross-functional teams that contain all the skills necessary to ship value for that domain: developers, QA, DBAs, and Product Owners. These teams should be small, typically adhering to Jeff Bezos’s "Two-Pizza Rule" (approx. 5-9 people), which aligns with Dunbar’s number limits for tight trust circles.2

Restrict Inter-Team Communication: Paradoxically, reducing the bandwidth between teams encourages the decoupling of the software. If Team A cannot easily talk to Team B to negotiate a schema change, they will be forced to define a clear, stable, and versioned API contract to communicate. The friction of social communication forces the formalization of technical interfaces.13

#### Critique and Limitations:

The ICM is not a magic wand. As pointed out by Mathias Verraes, "A reorganisation can't fix a broken design" if the system is already rigid.14 Attempting to reorganize teams around a codebase that is a "Big Ball of Mud" without simultaneously refactoring the code will result in "cognitive dissonance" where the team structure fights the code structure. The code will demand coordination that the organization chart discourages, leading to frustration and lower velocity.11 Therefore, the ICM must be accompanied by a technical strategy (like the Strangler Fig Pattern) to align the code with the new team boundaries.

## 2.3 Case Studies in Entropy

Theoretical definitions are necessary, but historical examples are instructional. The industry is replete with examples of distributed monoliths, particularly in sectors with heavy regulatory burdens and legacy inertia.

### 2.3.1 Case Study: The Banking Digital Transformation Failure
Context: A composite analysis of Tier-1 banks attempting "Digital Decoupling" from Mainframes (2018-2023).4

#### The Strategy:

Facing existential pressure from fintech challengers, many global banks adopted a strategy of placing an "Anti-Corruption Layer" (ACL) or API Gateway in front of their legacy Core Banking Systems (Mainframes). They then spun up hundreds of microservices to handle new digital channels (Mobile App, Web), aiming for agility and rapid feature release.
The Trap (The Shared Database):
Instead of migrating data out of the mainframe, the new microservices were often configured to read directly from a replicated Operational Data Store (ODS) or a Change Data Capture (CDC) stream that mirrored the legacy schema.

#### Result: 

The microservices were effectively coupled to the legacy data model. When the mainframe schema changed (e.g., expanding the AccountNumber field from 10 to 12 digits), 50+ microservices broke simultaneously because they shared the underlying data definition.
Data Sovereignty Violation: No single service owned the customer data. Validations were duplicated across services, leading to data corruption where the "Loan Service" allowed a transaction that the "Core Ledger" rejected hours later.4
The Outcome:

Development velocity initially spiked but stalled within 18 months. Deployments became "fear-driven," requiring "Release Train" coordination meetings involving 40+ stakeholders—the hallmark of a distributed monolith. The banks had built a distributed system that retained the fragility of the mainframe, adding network latency without achieving decoupling.

### 2.3.2 Case Study: Segment’s Retreat to the Monolith

#### Context:

Segment, a customer data platform, famously migrated back from microservices to a monolith in 2017, providing a crucial counter-narrative to the microservices hype cycle.19

#### The Problem:

Segment decomposed their ingestion worker into nanoservices based on destination (e.g., a worker for Google Analytics, a worker for Salesforce, etc.). This resulted in hundreds of repositories and services for a relatively small engineering team.

Operational Complexity: The team found themselves spending more time managing the orchestration of these services (auto-scaling groups, load balancers, version conflicts, library updates) than writing feature code.

The "Distributed Monolith" Symptom: They realized that the services were not truly independent; a change in the core library often required redeploying all 140+ services to ensure compatibility. The overhead of the network and the cognitive load of managing the fleet outweighed the benefits of isolation.

#### The Lesson:
Microservices solve a scale problem (too many developers stepping on each other's toes in one codebase), not a complexity problem. If a team is small, the operational overhead of microservices is a tax on velocity. Segment consolidated back into a modular monolith, reducing their operational overhead significantly while maintaining modularity via code boundaries rather than network boundaries.19

### 2.3.3 Case Study: Uber’s "DOMA" Evolution

#### Context:

Uber scaled to over 4,000 microservices, creating a "Dependency Hell" where understanding the impact of a change became impossible. The call graph was so complex that no single engineer could understand the path of a request.1

#### The Pivot:

Uber did not return to a monolith but evolved to Domain-Oriented Microservices Architecture (DOMA). This strategy represents a middle ground. They grouped related microservices (nanoservices) into "Domains" (Macroservices).

#### Gateways: 

Each domain (e.g., "Rider Management") exposes a single Gateway API. Internal complexity is hidden behind this gateway.

#### Clustering: 

Related services are clustered together, and strict rules govern communication between domains.

#### Lesson: 

There is a "Goldilocks" size for services. Too large (Monolith) and you lock up; too small (Nanoservice) and you drown in complexity. Uber's evolution demonstrates that structure must evolve with scale; what works for 100 engineers fails for 1,000.

## 2.4 Cognitive Load and Team Topologies

To avoid the Nanoservice trap and the Distributed Monolith, Architects must use Cognitive Load Theory as a primary design constraint. It is not enough for the software to be decoupled; the teams managing it must have the mental capacity to own it effectively.

### 2.4.1 Types of Cognitive Load in Software

Derived from John Sweller’s psychology research (1988), this framework is crucial for sizing microservices and defining team boundaries.2
Load Type
Definition
Software Example
Architect's Goal
Intrinsic
The inherent difficulty of the task itself.
Understanding the complex business rules of "Mortgage Calculation" or "Risk Analysis."
Manage: This cannot be removed, but it can be isolated via Bounded Contexts so only one team needs to bear it.
Extraneous
The load generated by the environment, tools, and format of information.
Remembering kubectl commands, configuring CI/CD YAML, managing retries, debugging obscure network flakes.
Minimize: Use Platform Engineering to abstract this away. This is "waste" that distracts from value.
Germane
The effort dedicated to creating schemas, mental models, and deep understanding.
Learning how the new "Payment" feature interacts with "Ledger" to optimize the business flow.
Maximize: This is where value creation happens. Teams should spend their mental energy here.

#### The Anti-Pattern Connection:

When a system is decomposed into Nanoservices, Extraneous Cognitive Load explodes. Developers must keep mental models of 50 different services, their ports, their deployment nuances, and their log locations. When Extraneous load exceeds the team's working memory, bug rates increase, and burnout sets in. The team enters "survival mode," refusing to refactor or improve the system because they are overwhelmed by the mechanics of keeping it running.24

#### 2.4.2 Team Topologies and the Team API

To manage cognitive load, the Team Topologies framework (Skelton & Pais) introduces specific team structures and interaction modes. A critical tool for preventing the Distributed Monolith is the Team API.25
Just as software has an API to define how it interacts with the world, a team should explicitly define its "API" to the rest of the organization. This reduces the "fuzzy ownership" that leads to tight coupling. 

A Team API should explicitly document:
Code: What repositories do we own?
Versioning: How do we communicate changes? (e.g., Semantic Versioning, Changelogs).
Communication: How do others reach us? (Slack channels, JIRA boards, Office Hours).
Practices: What are our testing standards? How do we handle on-call rotation?
By formalizing the Team API, we reduce the social coupling between teams. Team A doesn't need to tap Team B on the shoulder (high bandwidth) to ask "how do I use your service?"; they read the API documentation (low bandwidth). This promotes the "X-as-a-Service" interaction mode, which is essential for scaling.


Template: Team API Definition (Markdown)
Below is a standardized template for defining a Team API, adaptable for internal developer portals like Backstage.io 26:
Team API:

1. Identity & Focus
Team Name: Checkout Experience
Type: Stream-Aligned Team
Mission: To provide a seamless, one-click checkout experience for mobile and web users.
Bounded Context: Checkout, Cart, Payment Orchestration.

2. Communication Channels
Slack: #team-checkout-dev (Public discussion), #team-checkout-alerts (Incidents)
Sync: Daily Standup @ 10:00 AM EST (Zoom Link)
Request Method: JIRA Ticket (Project KEY: CHK) for non-urgent work.

3. Owned Services & Artifacts
Service Name
Repo Link
API Docs (Swagger/OpenAPI)
On-Call Schedule

checkout-api
[git/checkout-api]
[docs/checkout-api]


cart-service
[git/cart-service]
[docs/cart-service]



4. Versioning & Release
Strategy: Semantic Versioning (SemVer).
Deprecation Policy: We support the previous major version for 3 months.
Release Cadence: On-demand (CI/CD).

5. Testing & Quality
Contract Testing: We require Pact contracts for all consumers of checkout-api.
Performance: All endpoints must respond < 200ms (p99).
Implementing this simple document for every team forces the organization to confront ownership gaps. If a service like "Legacy-User-Db" cannot be assigned to a specific Team API, it is an orphan—a prime candidate for the decay that creates a distributed monolith.

## 2.5 Technical Remediation: Consumer-Driven Contract Testing (CDCT)

A primary symptom of the Distributed Monolith is the reliance on End-to-End (E2E) integration tests to verify correctness. These tests are slow, flaky, and require a full environment (the "Integration Database" again). When teams rely on E2E tests, they often freeze deployments because "the staging environment is unstable," leading to the lock-step deployment anti-pattern.
The cure is Consumer-Driven Contract Testing (CDCT) using tools like Pact.29

### 2.5.1 The Pattern

CDCT inverts the testing pyramid. Instead of the Provider (API Owner) guessing what the Consumers need, the Consumers explicitly define their expectations.
Consumer (e.g., Billing Service): Defines expectations (a "Contract") of what it needs from the Provider (e.g., User Service). "I expect GET /user/1 to return { 'id': '1', 'role': 'ADMIN' }."
Pact Broker: The contract is generated during the Consumer's unit tests and uploaded to a central broker (e.g., PactFlow).
Provider (User Service): During its own independent build, the Provider downloads the contract and replays the request against itself to ensure it complies.
This decouples the build pipelines. If the "User Service" team decides to rename role to user_role, their build fails immediately because it violates the contract with "Billing." No E2E environment is needed; the feedback is instant and local.

### 2.5.2 Expanded Code Example: CDCT with Pact (Java + JUnit 5)
The following example demonstrates a robust implementation of CDCT for a banking scenario. The LoanService (Consumer) checks if a customer is eligible by calling the CreditScoreService (Provider).
Consumer Side: Loan Service
The consumer test defines the "Pact" (the contract). It mocks the provider locally using Pact's mock server.
Dependency (Maven):

XML

<dependency>
    <groupId>au.com.dius.pact.consumer</groupId>
    <artifactId>junit5</artifactId>
    <version>4.6.2</version> <scope>test</scope>
</dependency>


Test Implementation (LoanConsumerTest.java):

Java


import au.com.dius.pact.consumer.MockServer;
import au.com.dius.pact.consumer.dsl.PactDslWithProvider;
import au.com.dius.pact.consumer.junit5.PactConsumerTestExt;
import au.com.dius.pact.consumer.junit5.PactTestFor;
import au.com.dius.pact.core.model.V4Pact;
import au.com.dius.pact.core.model.annotations.Pact;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.web.client.RestTemplate;
import java.util.HashMap;
import java.util.Map;
import static org.assertj.core.api.Assertions.assertThat;

// Extension to start the Pact Mock Server [31, 32]
@ExtendWith(PactConsumerTestExt.class) 
@PactTestFor(providerName = "CreditScoreService")
public class LoanConsumerTest {

    @Pact(consumer = "LoanService")
    public V4Pact createPact(PactDslWithProvider builder) {
        Map<String, String> headers = new HashMap<>();
        headers.put("Content-Type", "application/json");

        return builder
            // 'given' defines the state the provider must be in. This is crucial for 
            // avoiding the "Shared Database" anti-pattern. 
           .given("Customer 123 has a high credit score") 
           .uponReceiving("A request for credit check")
           .path("/credit-scores/123")
           .method("GET")
           .willRespondWith()
           .status(200)
           .headers(headers)
            // We define the body we expect. Pact will generate regex matchers 
            // to ensure strict adherence to types (int vs string).
           .body("{\"customerId\": \"123\", \"score\": 850, \"status\": \"EXCELLENT\"}")
           .toPact(V4Pact.class); // Explicitly returning V4 Pact [32]
    }

    @Test
    @PactTestFor(pactMethod = "createPact")
    void testCreditCheck(MockServer mockServer) {
        // This runs against the local Pact Mock Server, not the real provider.
        // It validates that our LoanService code effectively handles the response 
        // defined in the Pact.
        RestTemplate restTemplate = new RestTemplate();
        String url = mockServer.getUrl() + "/credit-scores/123";
        
        CreditScoreResponse response = restTemplate.getForObject(url, CreditScoreResponse.class);
        
        assertThat(response.getScore()).isEqualTo(850);
        assertThat(response.getStatus()).isEqualTo("EXCELLENT");
    }
}


Provider Side: Credit Score Service
The provider test downloads the Pact file and verifies that the actual controller code fulfills the contract.
Dependency (Maven):

XML


<dependency>
    <groupId>au.com.dius.pact.provider</groupId>
    <artifactId>junit5</artifactId>
    <version>4.6.2</version>
    <scope>test</scope>
</dependency>


Verification Implementation (CreditScoreProviderTest.java):

Java


import au.com.dius.pact.provider.junit5.PactVerificationContext;
import au.com.dius.pact.provider.junit5.PactVerificationInvocationContextProvider;
import au.com.dius.pact.provider.junitsupport.Provider;
import au.com.dius.pact.provider.junitsupport.State;
import au.com.dius.pact.provider.junitsupport.loader.PactFolder;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.TestTemplate;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.web.server.LocalServerPort;
import org.springframework.test.context.junit.jupiter.SpringExtension;

@ExtendWith(SpringExtension.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@Provider("CreditScoreService") // Must match the consumer's test [34, 35]
// In a real pipeline, use @PactBroker(host="...") to fetch dynamic pacts.
// @PactFolder is used here for local demonstration.
@PactFolder("target/pacts") 
public class CreditScoreProviderTest {

    @LocalServerPort
    int port;

    @BeforeEach
    void setup(PactVerificationContext context) {
        // Tell Pact where the real (running) provider is so it can send requests to it
        context.setTarget(new au.com.dius.pact.provider.junit5.HttpTestTarget("localhost", port));
    }

    @TestTemplate
    @ExtendWith(PactVerificationInvocationContextProvider.class) // 
    void pactVerificationTestTemplate(PactVerificationContext context) {
        // Dynamically generates tests for every interaction in the Pact file
        context.verifyInteraction();
    }

    // This method handles the state defined in the Consumer test.
    // It is executed BEFORE the request is replayed.
    @State("Customer 123 has a high credit score")
    public void setupHighCreditScoreState() {
        // Magic happens here: Use dependency injection (e.g., Mockito) to mock the 
        // internal repository or data store to return the specific data needed.
        // repository.save(new CreditScore("123", 850, "EXCELLENT"));
        
        // This ensures the service returns the data expected by the contract 
        // without relying on a brittle external database with pre-loaded data.
        System.out.println("State setup: Customer 123 -> 850");
    }
}


#### Benefits of this Approach:

Speed: No need to spin up the LoanService to test the CreditScoreService. The test runs in milliseconds.
Stability: No flaky network calls to external environments.
Governance: If the CreditScoreService developers change the "score" field from an Integer to a String, this test fails immediately in their Pull Request build. The breaking change is caught before it ever reaches a shared environment.36

## 2.6 Resilience Engineering: Beyond the Code

Escaping the distributed monolith requires accepting that failure is inevitable. In a distributed system, network partitions, latency spikes, and hardware failures are not anomalies; they are the steady state.

### 2.6.1 Chaos Engineering as an Architectural Requirement

The transition at Netflix from a monolithic DVD-rental application to a global streaming giant was predicated on the assumption of failure. They introduced the Simian Army—specifically Chaos Monkey—which randomly terminated production instances during business hours.1
This was not just a testing tool; it was a policy enforcement engine. By killing instances, Netflix forced developers to design stateless services. If a developer built a service that required "sticky sessions" or local disk storage, it would break immediately in production, and they would be forced to re-architect it to use externalized state (e.g., Cassandra, Memcached).

#### Modern Implementation (AWS FIS):

Today, we do not need to build custom monkeys. AWS Fault Injection Service (FIS) allows us to define experiments as code, integrated directly into the CI/CD pipeline.
Example Experiment Template (AWS FIS JSON):

JSON


{
  "description": "Terminate 20% of OrderService instances to test auto-scaling",
  "targets": {
    "OrderServiceInstances": {
      "resourceType": "aws:ec2:instance",
      "resourceTags": { "Service": "OrderService", "Env": "Staging" },
      "selectionMode": "percent(20)"
    }
  },
  "actions": {
    "terminateInstances": {
      "actionId": "aws:ec2:terminate-instances",
      "parameters": {},
      "targets": { "Instances": "OrderServiceInstances" }
    }
  },
  "stopConditions":
}


#### The Architect's Rule: A microservice is not "Production Ready" until it has survived a Chaos Experiment in the staging environment. This prevents the "Fragile Monolith" anti-pattern where services are nominally distributed but operationally fragile.

## Conclusion
The Distributed Monolith is not a technical accident; it is an organizational mirror. It emerges when teams adopt the syntax of microservices (Docker, Kubernetes, REST) without adopting the grammar of distributed systems (Bounded Contexts, Asynchrony, Eventual Consistency, Decentralized Governance).
To expand beyond Chapter 2 is to recognize that architecture is a feedback loop:
Organization shapes Architecture (Conway's Law).

Architecture imposes Cognitive Load.

Cognitive Load determines Team Performance.
The role of the Senior Architect is to intervene in this loop—using tools like the Inverse Conway Maneuver, Consumer-Driven Contracts, and Polyglot Persistence—to ensure that the system remains a set of loosely coupled services, rather than a fragmented, distributed nightmare. The recipes provided here—specific code implementations, historical warnings, and mathematical models—are the weapons against this entropy.

Key Terminology Reference
Term
Definition
Inverse Conway Maneuver
The strategy of restructuring teams to promote a desired software architecture.
Homomorphism
The structural mapping between organization and system design, preserving relationships.
Connascence
A metric for software coupling strength (Identity, Meaning, Timing).
Pact
A tool for consumer-driven contract testing (CDCT) to decouple build pipelines.
Cognitive Load
The mental effort required to perform a task (Intrinsic, Extraneous, Germane).
Distributed Monolith
A system with microservice deployment artifacts but monolithic coupling characteristics.
Team API
A defined interface for team interaction (code, documentation, communication) to reduce social coupling.



----------------------------------------------------

## Table of Contents

* [Definition](#definition)
* [Why-Microservice](#Why-Microservice)
* [When-to-use-microservice-architecture](#When-to-use-microservice-architecture)
* [Pros-and-cons](#pros-and-cons)
* [Microservice-Design-Guidelines](#guidelines)
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

* Microservice make our system loosely coupled, i.e. if we need to update, repair, or replace a Microservice, we don't need to rebuild our entire application, just swap out the part that needs it.
* To built each Microservice can use different languages and tools. Microservices communicate with well defined interface
* The communication should be stateless for scalability(copies of Microservice) and reliability(one copy fail other copy can serve), the most common methods for communication between Microservices are HTTP and messaging.
Each Microservice should have it's own datastore.
* Small team capable to work on design, web development, coding, database admin and operations.

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

* Start withrelatively broad service boundaries to begin with, refactoring to smaller ones (based on business requirements) 
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
* [Server-side discovery from Chris Richardson ](http://microservices.io/patterns/apigateway.html)
* [Service registry from Chris Richardson](http://microservices.io/patterns/apigateway.html)
* [Self registration from Chris Richardson](http://microservices.io/patterns/apigateway.html)
* [3rd party registration from Chris Richardson](http://microservices.io/patterns/apigateway.html)
* [Service discovery with consul & etcd](https://aws.amazon.com/blogs/compute/service-discovery-via-consul-with-amazon-ecs/)

#### Service Mesh

* [What Is a Service Mesh](https://www.nginx.com/blog/what-is-a-service-mesh/)
* [istio](https://istio.io/docs/concepts/what-is-istio/)
* [Service mesh vs api getway](https://medium.com/microservices-in-practice/service-mesh-vs-api-gateway-a6d814b9bf56)
* [Service Mesh With Istio on Kubernetes in 5 Steps](https://dzone.com/articles/service-mesh-with-istio-on-kubernetes-in-5-steps)


#### Strategies and patterns for realizing the seven design guidelines applied to microservices (sei.cmu.edu)

#### Standardized service contract. Strategies include:
* [REST API design best practices](#pragmatic-rest)
* [API gateway](https://apigee.com/about/cp/api-gateway)    
* [contract-first design](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.435.2220&rep=rep1&type=pdf)     

#### Service loose coupling. Strategies include:
* [Service Facade pattern](https://www.ibm.com/support/knowledgecenter/pt-br/SSMKHH_9.0.0/com.ibm.etools.mft.pattern.sen.doc/sen/sf/overview.htm)  
* [Legacy Wrapper pattern](https://patterns.arcitura.com/soa-patterns/design_patterns/legacy_wrapper) 
* [point-to-point, publish-subscribe and other messaging patterns](https://hackernoon.com/observer-vs-pub-sub-pattern-50d3b27f838c)  
* [event-driven architecture](https://microservices.io/patterns/data/event-driven-architecture.html)  

#### Service reusability. Strategies include:
* [modeling for reuse](#)  
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

### Certify-microservices-design :

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
      
   ![Alt Text](https://spring.io/img/homepage/diagram-distributed-systems.svg)
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
    



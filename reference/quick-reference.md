# Quick Reference

## Essential Patterns and Practices for Microservices Architecture

This quick reference provides at-a-glance guidance for common microservices patterns, best practices, and decision points. Use this as a handy reference during design sessions, code reviews, and architectural discussions.

---

## 🏗️ Design Principles

### Core Principles Checklist
- [ ] **Single Responsibility**: Each service has one reason to change
- [ ] **Loose Coupling**: Minimal dependencies between services
- [ ] **High Cohesion**: Related functionality grouped together
- [ ] **Autonomy**: Independently deployable and scalable
- [ ] **Resilience**: Designed to handle failures gracefully

### Khan Pattern Decision Matrix

| Factor | Fine-Grained | Medium-Grained | Coarse-Grained |
|--------|--------------|----------------|----------------|
| **Complexity** | High | Medium | Low |
| **Change Frequency** | High | Medium | Low |
| **Team Capacity** | Multiple Teams | Single Team | Shared Team |
| **Scaling Needs** | Independent | Moderate | Uniform |
| **Data Coupling** | Low | Medium | High |

**Decision Rule**: Choose granularity based on your organizational context, not rigid rules.

---

## 📡 Communication Patterns

### Synchronous vs Asynchronous

| Aspect | Synchronous | Asynchronous |
|--------|-------------|--------------|
| **Coupling** | Higher | Lower |
| **Latency** | Direct | Indirect |
| **Resilience** | Lower | Higher |
| **Complexity** | Lower | Higher |
| **Use Cases** | Real-time queries | Event processing |

### Communication Pattern Selection

```
Query Data → REST/GraphQL
Commands → Async Messages
Events → Event Streaming
Real-time → WebSockets/gRPC
```

### REST API Best Practices

```http
# Good URLs
GET /api/v1/orders/123
POST /api/v1/orders
PUT /api/v1/orders/123
DELETE /api/v1/orders/123

# Bad URLs
GET /api/getOrder?id=123
POST /api/createOrder
PUT /api/updateOrder
DELETE /api/deleteOrder
```

---

## 🗄️ Data Management Patterns

### Database per Service Rules
- ✅ Each service owns its database
- ✅ Access data only through service APIs
- ❌ Never share databases between services
- ❌ No direct database access from other services

### Data Consistency Patterns

| Pattern | Use Case | Complexity | Consistency |
|---------|----------|------------|-------------|
| **Strong Consistency** | Financial transactions | High | Immediate |
| **Eventual Consistency** | User profiles | Medium | Delayed |
| **Saga Pattern** | Multi-service workflows | High | Compensating |
| **Event Sourcing** | Audit trails | High | Event-based |

### CQRS Decision Tree

```
Need different read/write models? → Yes → Consider CQRS
High read/write ratio? → Yes → Consider CQRS
Complex queries? → Yes → Consider CQRS
Simple CRUD? → No → Skip CQRS
```

---

## 🛡️ Resilience Patterns

### Essential Resilience Patterns

| Pattern | Purpose | When to Use |
|---------|---------|-------------|
| **Circuit Breaker** | Prevent cascade failures | External service calls |
| **Retry** | Handle transient failures | Network operations |
| **Timeout** | Prevent hanging requests | All remote calls |
| **Bulkhead** | Isolate resources | Critical vs non-critical |
| **Fallback** | Graceful degradation | User-facing features |

### Circuit Breaker States

```
CLOSED → Normal operation
OPEN → Failing fast (no calls)
HALF-OPEN → Testing recovery
```

### Retry Strategy

```python
# Exponential backoff with jitter
delay = base_delay * (2 ** attempt) + random_jitter
max_attempts = 3
```

---

## 🔍 Service Discovery

### Discovery Patterns

| Pattern | Pros | Cons | Best For |
|---------|------|------|----------|
| **Client-Side** | Simple, fast | Client complexity | Internal services |
| **Server-Side** | Client simplicity | Additional hop | External clients |
| **Service Mesh** | Rich features | Operational complexity | Large deployments |

### Health Check Endpoints

```http
GET /health
{
  "status": "UP",
  "checks": {
    "database": "UP",
    "external-service": "DOWN"
  }
}
```

---

## 🔐 Security Patterns

### Authentication & Authorization

```
API Gateway → JWT Validation → Service Authorization
```

### Security Checklist
- [ ] Use HTTPS everywhere
- [ ] Implement JWT token validation
- [ ] Apply principle of least privilege
- [ ] Secure service-to-service communication
- [ ] Implement rate limiting
- [ ] Log security events

### JWT Token Structure

```json
{
  "header": {
    "alg": "RS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "user123",
    "iat": 1516239022,
    "exp": 1516242622,
    "roles": ["user", "admin"]
  }
}
```

---

## 📊 Observability

### Three Pillars of Observability

1. **Metrics** → What is happening?
2. **Logs** → Why is it happening?
3. **Traces** → Where is it happening?

### Essential Metrics

| Type | Examples | Purpose |
|------|----------|---------|
| **Business** | Orders/minute, Revenue | Business health |
| **Application** | Response time, Error rate | App performance |
| **Infrastructure** | CPU, Memory, Disk | Resource usage |

### Distributed Tracing

```
Request ID: 12345
├── Service A (10ms)
├── Service B (50ms)
│   ├── Database Query (30ms)
│   └── External API (15ms)
└── Service C (25ms)
```

### Log Levels

```
ERROR → System errors, exceptions
WARN → Potential issues, degraded performance
INFO → Important business events
DEBUG → Detailed diagnostic information
```

---

## 🚀 Deployment Patterns

### Deployment Strategies Comparison

| Strategy | Downtime | Risk | Complexity | Rollback |
|----------|----------|------|------------|----------|
| **Blue-Green** | None | Low | Medium | Instant |
| **Canary** | None | Very Low | High | Gradual |
| **Rolling** | None | Medium | Low | Gradual |
| **Recreate** | Yes | High | Low | Manual |

### Container Best Practices

```dockerfile
# Multi-stage build
FROM node:16-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:16-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
EXPOSE 3000
USER node
CMD ["npm", "start"]
```

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-service
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
  template:
    spec:
      containers:
      - name: my-service
        image: my-service:v1.0
        ports:
        - containerPort: 8080
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
```

---

## 🧪 Testing Strategies

### Testing Pyramid for Microservices

```
    /\
   /  \  E2E Tests (Few)
  /____\
 /      \ Integration Tests (Some)
/__________\ Unit Tests (Many)
```

### Test Types

| Test Type | Scope | Speed | Cost | Purpose |
|-----------|-------|-------|------|---------|
| **Unit** | Single function | Fast | Low | Logic validation |
| **Integration** | Service boundaries | Medium | Medium | Interface validation |
| **Contract** | API contracts | Fast | Low | API compatibility |
| **E2E** | Full workflow | Slow | High | User journey validation |

### Contract Testing

```yaml
# Consumer contract
interactions:
- description: "Get user by ID"
  request:
    method: GET
    path: /users/123
  response:
    status: 200
    body:
      id: 123
      name: "John Doe"
```

---

## ⚠️ Anti-Patterns to Avoid

### Common Anti-Patterns

| Anti-Pattern | Description | Solution |
|--------------|-------------|----------|
| **Distributed Monolith** | Tightly coupled services | Proper service boundaries |
| **Chatty Services** | Too many service calls | Coarser-grained interfaces |
| **Shared Database** | Multiple services, one DB | Database per service |
| **Lack of Automation** | Manual deployments | CI/CD pipelines |
| **Premature Decomposition** | Too many small services | Start with monolith |

### Warning Signs

🚨 **Red Flags**:
- Services always deployed together
- Frequent cross-service database queries
- Cascading failures
- Long deployment times
- Difficulty tracing requests

---

## 📏 Sizing Guidelines

### Service Size Indicators

**Too Small** (Nano-service):
- Single function services
- High communication overhead
- Difficult to maintain

**Too Large** (Mini-monolith):
- Multiple business capabilities
- Large team required
- Difficult to deploy independently

**Just Right**:
- Single business capability
- Owned by one team
- Independently deployable
- Clear boundaries

### Team Size Rule

```
Team Size = 2-8 people (Amazon's "Two Pizza Rule")
Services per Team = 1-3 services
```

---

## 🔧 Technology Stack Recommendations

### Popular Technology Combinations

**Java Ecosystem**:
```
Spring Boot + Spring Cloud
Netflix OSS (Eureka, Hystrix, Zuul)
Apache Kafka + Docker + Kubernetes
```

**Node.js Ecosystem**:
```
Express.js + Consul
RabbitMQ + Docker + Kubernetes
```

**Polyglot Approach**:
```
API Gateway: Kong/Ambassador
Service Mesh: Istio/Linkerd
Monitoring: Prometheus + Grafana
Logging: ELK Stack
```

---

## 📋 Decision Checklists

### Microservices Readiness Checklist

**Organizational Readiness**:
- [ ] DevOps culture and practices
- [ ] Automated testing and deployment
- [ ] Monitoring and alerting capabilities
- [ ] Team autonomy and ownership
- [ ] Failure handling processes

**Technical Readiness**:
- [ ] Container orchestration platform
- [ ] Service discovery mechanism
- [ ] API gateway solution
- [ ] Distributed tracing system
- [ ] Centralized logging

### Service Boundary Checklist

- [ ] Aligns with business capability
- [ ] Can be owned by single team
- [ ] Has clear data ownership
- [ ] Minimal dependencies on other services
- [ ] Can be deployed independently

---

## 🎯 Quick Wins

### Start Here (Low Risk, High Value)

1. **Extract Read-Only Services**: Start with services that only read data
2. **Implement API Gateway**: Centralize cross-cutting concerns
3. **Add Health Checks**: Enable better monitoring and deployment
4. **Implement Circuit Breakers**: Improve system resilience
5. **Centralize Logging**: Improve observability

### Avoid These Initially (High Risk)

1. **Distributed Transactions**: Complex and error-prone
2. **Event Sourcing**: High complexity for beginners
3. **Fine-Grained Services**: Start coarser, refine later
4. **Custom Service Mesh**: Use proven solutions first

---

## 📚 Essential Resources

### Must-Read Books
1. "Building Microservices" - Sam Newman
2. "Microservices Patterns" - Chris Richardson
3. "Domain-Driven Design" - Eric Evans

### Key Websites
- microservices.io - Pattern catalog
- 12factor.net - Application methodology
- martinfowler.com - Architecture insights

### Tools to Evaluate
- **API Gateways**: Kong, Ambassador, Zuul
- **Service Mesh**: Istio, Linkerd, Consul Connect
- **Monitoring**: Prometheus, Grafana, Jaeger
- **Orchestration**: Kubernetes, Docker Swarm

---

## 🆘 Troubleshooting Guide

### Common Issues and Solutions

| Problem | Symptoms | Solution |
|---------|----------|----------|
| **Cascade Failures** | Multiple services failing | Implement circuit breakers |
| **Slow Responses** | High latency | Add caching, optimize queries |
| **Data Inconsistency** | Stale data | Implement eventual consistency |
| **Deployment Issues** | Failed deployments | Improve health checks |
| **Monitoring Gaps** | Unknown system state | Add distributed tracing |

### Performance Optimization

1. **Cache Frequently Accessed Data**
2. **Use Async Communication Where Possible**
3. **Implement Connection Pooling**
4. **Optimize Database Queries**
5. **Use CDN for Static Content**

---

*This quick reference is designed to be printed or bookmarked for easy access during development. For detailed explanations, refer to the full chapters in this book.*

**Last Updated**: February 2026

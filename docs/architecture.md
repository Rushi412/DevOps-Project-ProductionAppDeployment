```mermaid
flowchart LR
    User["User Browser"]
    App["Spring Boot Social Platform App<br/>Java 17 • Thymeleaf • Spring Security"]
    DB["H2 (local)<br/>PostgreSQL (future prod profile)"]
    Docker["Docker multi-stage image"]
    Kind["kind Kubernetes cluster<br/>namespace: social-app"]
    Jenkins["Jenkins CI/CD"]
    Trivy["Trivy security scan"]
    DockerHub["Docker Hub<br/>rushi412/social-platform-app"]

    User --> App
    App --> DB
    App --> Docker
    Docker --> Kind
    Jenkins --> App
    Jenkins --> Trivy
    Jenkins --> DockerHub
    DockerHub --> Kind
```
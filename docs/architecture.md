# Architecture

```text
Developer -> GitHub -> Jenkins -> Maven tests -> Docker image -> Docker Hub
                                                    |
                                                    v
                                        kind Kubernetes (social-app)
                                                    |
                                                    v
                                           Spring Boot Social Platform App
```

The application is a Spring Boot 3 application with Spring Security, Thymeleaf, JPA, and Actuator. Local development uses H2. Development and production database credentials are read from environment variables.

Terraform in `infrastructure/terraform` is an optional EKS learning exercise. It provisions billable AWS resources and must only be applied after reviewing the Terraform plan and AWS pricing. The supported no-cost path is the standalone kind cluster described in `deploy/kubernetes/local`.

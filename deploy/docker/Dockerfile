FROM maven:3.9.9-eclipse-temurin-17-alpine AS build

WORKDIR /workspace
COPY pom.xml ./
RUN mvn dependency:go-offline
COPY src src
RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jre-alpine

WORKDIR /app
RUN apk upgrade --no-cache
RUN addgroup -S spring && adduser -S spring -G spring
COPY --from=build /workspace/target/*.jar app.jar

USER spring
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/app.jar"]

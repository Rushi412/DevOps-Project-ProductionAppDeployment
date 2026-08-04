import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  scenarios: {
    health_smoke: {
      executor: "ramping-vus",
      stages: [
        { duration: "15s", target: 5 },
        { duration: "30s", target: 10 },
        { duration: "15s", target: 0 },
      ],
    },
  },
  thresholds: {
    http_req_failed: ["rate<0.01"],
    http_req_duration: ["p(95)<500"],
    checks: ["rate>0.99"],
  },
};

const baseUrl = __ENV.BASE_URL || "http://localhost:8080";

export default function () {
  const response = http.get(`${baseUrl}/actuator/health`);
  check(response, {
    "health endpoint returns 200": (result) => result.status === 200,
    "health response reports UP": (result) => result.body.includes('"status":"UP"'),
  });
  sleep(1);
}

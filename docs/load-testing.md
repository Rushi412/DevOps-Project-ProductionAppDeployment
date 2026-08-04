# Load-test evidence

The k6 smoke test in `tests/load/smoke.js` checks the Spring Boot health endpoint with a small ramp from 5 to 10 virtual users. It is intentionally safe for a local portfolio environment.

## Run

```powershell
$env:BASE_URL = 'http://localhost:8080'
k6 run --summary-export=build/k6-summary.json tests/load/smoke.js
```

## Acceptance criteria

- Fewer than 1% failed HTTP requests.
- At least 99% successful checks.
- 95th-percentile response time below 500 milliseconds.

No benchmark result is claimed until the test is run against a named environment. Commit the generated summary only when it contains reproducible results and no sensitive endpoints.

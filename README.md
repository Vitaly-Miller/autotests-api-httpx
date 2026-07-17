# API Automation Tests by Vitaly Miller

[![API tests](https://github.com/Vitaly-Miller/autotests-api-httpx/actions/workflows/tests.yml/badge.svg)](https://github.com/Vitaly-Miller/autotests-api-httpx/actions/workflows/tests.yml)

Automated REST API tests for the [API Test Server](https://github.com/Vitaly-Miller/autotests-api-server) —
application with users, courses, exercises and file storage.

Built with **Python**, **HTTPX**, **Pytest**, **Pydantic**, **Allure**, **Faker** and **Swagger Coverage Tool**.

---
- <img src="https://allurereport.org/svg/logo-report-sign.svg" height="12"> [My Allure Report](https://vitaly-miller.github.io/autotests-api-httpx/) — test results with history, published on GitHub Pages
- 📊 [My API Coverage Report](https://vitaly-miller.github.io/autotests-api-httpx/coverage.html) — endpoint coverage measured against the OpenAPI spec
- <img src="https://icon.icepanel.io/Technology/svg/Swagger.svg"  height="12"> [API Documentation (Swagger UI)](https://vitaly-miller.github.io/autotests-api-httpx/swagger.html) — interactive docs of the API under test
- 👨🏻‍💻 [My Code](https://github.com/Vitaly-Miller/autotests-api-httpx) — source code on GitHub
---

> **⚠️ A note on code comments.**  
> The code is deliberately annotated in detail — nearly every line
> carries a comment explaining what it does and why. This is an intentional choice for
> a portfolio project: it lets a reviewer follow every implementation decision without leaving the
> file. In production code I would keep comments far more sparing, reserving them for non-obvious
> constraints and decisions.

---
## ✨ Highlights

### 🏗️ Architecture
- **Layered design** — API clients, Pydantic schemas, fixtures and tests are strictly separated
- **API clients** built on HTTPX with event hooks that automatically instrument every request
- **API contract testing** — Pydantic models validate every request/response, plus JSON Schema checks
- **Reusable Pytest fixtures** for authentication, test entities and test data setup
- **Fake data generation** with Faker to simulate real-world scenarios

### 📋 Reporting & Observability
- **Allure reporting** with steps and run history, published on GitHub Pages
- **Rich per-request attachments** — request & response bodies and headers (pretty-printed JSON)
  and a ready-to-run **cURL command** for every API call
- **Logging** — every request and response is logged via a custom logger; pytest captures the log
  and Allure displays it in each test's log section
- **Swagger coverage** — every API call is tracked and matched against the OpenAPI spec

### 🧪 Test Design
- **Markers** by type (`smoke`, `regression`, `negative`) and by domain (`auth`, `users`, `courses`, …)
- **Parallel execution** (pytest-xdist) and **automatic reruns** of flaky tests (pytest-rerunfailures)
- **Test variants** — some scenarios are intentionally implemented in several variants to showcase
  different approaches: e.g. `TestCreateUser` covers the same flow via a full-cycle fixture (v.1),
  an API client fixture (v.2), parametrized (v.3), and fully manual (v.4); the `v.1`–`v.4` titles
  are visible in the Allure Report, making the implementations easy to compare side by side

### ⚙️ CI/CD
- **GitHub Actions pipeline** — starts a live API server, runs the full suite, and publishes the
  Allure and coverage reports to GitHub Pages with history preserved between runs

---

## Project Structure

```
├─ 📁 .github/       # CI/CD workflow (GitHub Actions)
├─ 📁 clients/       # API clients (auth, users, courses, exercises, files) built on HTTPX
├─ 📁 docs/          # Static Swagger UI page, published to GitHub Pages by CI
├─ 📁 schemas/       # Pydantic models for requests, responses and error bodies
├─ 📁 fixtures/      # Pytest fixtures (clients, users, courses, exercises, files)
├─ 📁 tests/         # Test suites grouped by domain: auth, users, courses, exercises, files
├─ 📁 tools/         # Assertions, Allure helpers, event hooks, data generator, logger
├─ 📁 testdata/      # Static test data (e.g. files for upload tests)
├─ config.py         # Typed settings loaded from .env via pydantic-settings
├─ conftest.py       # Root fixtures (via Pytest Plugins)
└─ pytest.ini        # Pytest configuration and markers

```
---
## Getting Started


### ⤵️ Clone the Repository

```bash
git clone https://github.com/Vitaly-Miller/autotests-api-httpx.git
cd autotests-api-httpx
```

### 🔘 Create a Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 🔀 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🖥️ Start the Test Server

The tests run against a locally started [API Test Server](https://github.com/Vitaly-Miller/autotests-api-server).
Clone it and start it in a separate terminal (see its README for details):

```bash
git clone https://github.com/Vitaly-Miller/autotests-api-server.git
cd autotests-api-server
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

The server is expected at `http://localhost:8000` — the base URL and other settings
are defined in [`.env`](.env) and loaded through `pydantic-settings` (see `config.py`).

## Running the Tests

Run the full suite with Allure results:

```bash
python -m pytest --alluredir=allure-results --clean-alluredir
```

### Selective Runs with Markers

Tests are tagged by type (`smoke`, `regression`, `negative`) and by domain
(`auth`, `users`, `courses`, `exercises`, `files`):

```bash
python -m pytest -m smoke                  # smoke tests only
python -m pytest -m "regression and users" # regression tests for the users domain
```

### Parallel Execution & Reruns

```bash
python -m pytest -n auto          # run in parallel (pytest-xdist)
python -m pytest --reruns 2       # retry flaky tests (pytest-rerunfailures)
```

## Reports

### <img src="https://allurereport.org/svg/logo-report-sign.svg" height="12"> Allure Report

```bash
allure serve allure-results
```

Opens an interactive report in your browser. Each test includes step-by-step execution details,
and every API call comes with attachments added automatically by HTTPX event hooks:

- request summary — URL, method, response status code;
- request & response **bodies** and **headers** as pretty-printed JSON;
- a ready-to-run **cURL command** to reproduce the request manually;
- the captured **log** of all requests and responses during the test.

### 📊 API Coverage Report

```bash
swagger-coverage-tool save-report
```

Generates `coverage.html` — which endpoints, methods and status codes are covered
compared to the server's OpenAPI spec, with history across runs.

## <img src="https://innovationspace.ansys.com/knowledge/wp-content/uploads/sites/4/2024/02/scade-009-ci-cd-workflow.svg"  height="16"> CI/CD 

Every push and pull request to `main` triggers the [GitHub Actions pipeline](.github/workflows/tests.yml):

1. **run-tests** — clones and starts the API Test Server, waits for it to become healthy,
   runs the full test suite and generates Allure results and the Swagger coverage report
   (coverage history is preserved between runs via the Actions cache);
2. **publish-report** — builds the Allure report with run history and deploys it together
   with the coverage report to [GitHub Pages](https://vitaly-miller.github.io/autotests-api-httpx/).

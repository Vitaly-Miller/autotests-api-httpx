# API Automation Tests by Vitaly Miller

[![API tests](https://github.com/Vitaly-Miller/autotests-api-httpx/actions/workflows/tests.yml/badge.svg)](https://github.com/Vitaly-Miller/autotests-api-httpx/actions/workflows/tests.yml)

Automated REST API tests for the [API Test Server](https://github.com/Vitaly-Miller/autotests-api-server) —
a training application with users, courses, exercises and file storage.

Built with **Python**, **HTTPX**, **Pytest**, **Pydantic**, **Allure**, **Faker** and **Swagger Coverage Tool**.

- 👉 [Allure Report](https://vitaly-miller.github.io/autotests-api-httpx/) — test results with history, published on GitHub Pages
- 👉 [API Coverage Report](https://vitaly-miller.github.io/autotests-api-httpx/coverage.html) — endpoint coverage measured against the OpenAPI spec
- 👉 [Code](https://github.com/Vitaly-Miller/autotests-api-httpx) — source code on GitHub

## Highlights

- **Layered architecture** — API clients, Pydantic schemas, fixtures and tests are strictly separated
- **API clients** built on HTTPX with event hooks for logging and Allure attachments
- **Pydantic models** for request/response validation and JSON Schema checks (API contract testing)
- **Reusable Pytest fixtures** for authentication, test entities and test data setup
- **Fake data generation** with Faker to simulate real-world scenarios
- **Allure reporting** with steps, attachments and run history
- **Swagger coverage** — every API call is tracked and matched against the OpenAPI spec
- **CI/CD** — GitHub Actions pipeline runs the full suite against a live server and publishes reports

## Project Structure

```
├── clients/       # API clients (auth, users, courses, exercises, files) built on HTTPX
├── schemas/       # Pydantic models for requests, responses and error bodies
├── fixtures/      # Pytest fixtures (clients, users, courses, exercises, files)
├── tests/         # Test suites grouped by domain: auth, users, courses, exercises, files
├── tools/         # Assertions, Allure helpers, event hooks, data generator, logger
├── testdata/      # Static test data (e.g. files for upload tests)
├── config.py      # Typed settings loaded from .env via pydantic-settings
├── conftest.py    # Root fixtures
├── pytest.ini     # Pytest configuration and markers
└── .github/       # CI/CD workflow (GitHub Actions)
```

## Getting Started

### Requirements

- Python 3.13+
- [Allure CLI](https://allurereport.org/docs/gettingstarted-installation/) — only needed to view Allure reports locally

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

### 📋 Allure Report

```bash
allure serve allure-results
```

Opens an interactive report in your browser: test steps, request/response attachments and logs.

### 📊 API Coverage Report

```bash
swagger-coverage-tool save-report
```

Generates `coverage.html` — which endpoints, methods and status codes are covered
compared to the server's OpenAPI spec, with history across runs.

## CI/CD

Every push and pull request to `main` triggers the [GitHub Actions pipeline](.github/workflows/tests.yml):

1. **run-tests** — clones and starts the API Test Server, waits for it to become healthy,
   runs the full test suite and generates Allure results and the Swagger coverage report
   (coverage history is preserved between runs via the Actions cache);
2. **publish-report** — builds the Allure report with run history and deploys it together
   with the coverage report to [GitHub Pages](https://vitaly-miller.github.io/autotests-api-httpx/).

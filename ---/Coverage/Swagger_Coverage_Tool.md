# Swagger Coverage Tool (Покрытие требований)

---
### 1. Установка библиотеки (модуля)
```shell
pip install swagger-coverage-tool
```
---

### 2. Настройки `.env` / `.json` / `.yaml`
### `.env`
```dotenv
# Указываем список сервисов, для которых будет измеряться покрытие
SWAGGER_COVERAGE_SERVICES='[
    {
        "key": "api-service",
        "name": "API Service",
        "tags": ["API", "PRODUCTION"],
        "repository": "https://github.com/Vitaly-Miller/autotests-api-httpx",
        "swagger_url": "http://localhost:8000/openapi.json"
        "swagger_file": "./openapi.json"   # (optional) Если файл локальный 
    }
]'
#------------- Default Settings (optional) ---------------    # (Если не нужно вообще - ...=null)
SWAGGER_COVERAGE_RESULTS_DIR="./coverage-results"             # Папка, в которую будут сохраняться промежуточные JSON-файлы покрытия
SWAGGER_COVERAGE_HISTORY_FILE="./coverage-history.json"       # Файл с историей покрытия по запускам
SWAGGER_COVERAGE_HISTORY_RETENTION_LIMIT=30                   # Ограничение на количество хранимых исторических записей (для отчёта в динамике)
SWAGGER_COVERAGE_HTML_REPORT_FILE="./index.html"              # Путь к итоговому HTML-отчёту (визуальный, открывается в браузере)
SWAGGER_COVERAGE_JSON_REPORT_FILE="./coverage-report.json"    # Путь к итоговому JSON-отчёту (для интеграций и CI)
```

### `swagger_coverage_config.json`
```json
{
  "services": [
    {
      "key": "api-service",
      "name": "API Service",
      "tags": ["API", "PRODUCTION"],
      "repository": "https://github.com/Vitaly-Miller/autotests-api-httpx",
      "swagger_url": "http://localhost:8000/openapi.json"
    }
  ],
  "results_dir": "./coverage-results",             
  "history_file": "./coverage-history.json",
  "history_retention_limit": 30,
  "html_report_file": "./index.html",
  "json_report_file": "./coverage-report.json"
}
```

### `swagger_coverage_config.yaml`
```yaml
# List of service configurations.
services:
  - key: "api-service"                                                    # Unique identifier for the service.
    name: "API Service"                                                   # Name of the service.
    tags: [ "API", "PRODUCTION" ]                                         # Optional list of tags to describe the service.
    repository: "https://github.com/Vitaly-Miller/autotests-api-httpx"    # Optional URL to the repository of the service.
    swagger_url: "http://localhost:8000/openapi.json"                     # Optional URL to the Swagger documentation.
    # swagger_file: "swagger_file_path.json"                              # Alternatively, you can provide a file path instead of a URL.

# Directory where coverage results will be stored.
results_dir: "./coverage-results"                       # This path is relative to the current working directory.

# File where the history of coverage results is saved.
history_file: "./coverage-history.json"                 # This path is relative to the current working directory.
history_retention_limit: 30                             # The maximum number of history records to keep.

# File paths for reports. These are optional, and if not set, reports will not be generated.
html_report_file: "./index.html"                        # Path to the HTML report file.
json_report_file: "./coverage-report.json"              # Path to the JSON report file.
```
---
### 3. Проверка конфигурации (вывод в консоль Терминала)
```shell
swagger-coverage-tool print-config
```

---
### 3. Пример использования
```python
import httpx
from swagger_coverage_tool import SwaggerCoverageTracker

#==================================================================================
# Инициализируем трекер для сервиса с ключом "api-service"
tracker = SwaggerCoverageTracker(service='api-service')   

# Оборачиваем функцию вызова GET-запроса в coverage_httpx@декоратор трекера 
@tracker.track_coverage_httpx("/api/v1/users/{user_id}")   # + ENDPOINT из Swagger❗️
def get_user(user_id: str) -> httpx.Response:
    return httpx.get(f"http://localhost:8000/api/v1/users/{user_id}")

#--------------
# Вызываем функцию, чтобы она попала в отчет покрытия
get_user('123')
```

### 3.1  Пример использования (Для нескольких микросервисов)
```python
import httpx
from swagger_coverage_tool import SwaggerCoverageTracker

#==================================================================================
tracker_users = SwaggerCoverageTracker(service="users-service")        # Инициализация трекера для Users
tracker_payments = SwaggerCoverageTracker(service="payments-service")  # Инициализация трекера для Payments

@tracker_users.track_coverage_httpx("/api/v1/users")                   # Декоратор для Users
def create_user() -> httpx.Response:
    return httpx.post("http://localhost:8001/api/v1/users")

@tracker_payments.track_coverage_httpx("/api/v1/payments")             # Декоратор для Payments
def make_payment() -> httpx.Response:
    return httpx.post("http://localhost:8002/api/v1/payments")

#--------------
# Вызываем функции, чтобы они попали в отчет покрытия
create_user()
make_payment()
```


#### В корне проекта появится папка с Результатами покрытия:
- `📁`[coverage-results/]() `Результаты`
---

### 4. Генерация Отчета покрытия
```shell
swagger-coverage-tool save-report
```

#### В корне проекта появится файлы:

- [coverage-history.json]() `История`
- [coverage-report.json]() `Отчет`
- [index.html]() `Файл открытия отчета`



---

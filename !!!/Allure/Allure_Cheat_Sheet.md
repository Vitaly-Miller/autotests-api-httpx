# Allure Cheat Sheet

## Установка
-   **allure-pytest** — Python-плагин для pytest, который собирает
    результаты тестов в папку `allure-results`.
-   **Allure CLI** — инструмент для генерации и просмотра
    HTML-отчётов.

```
pip install allure-pytest
brew install allure
```

Проверка версии
```
allure --version
```

Обновление
```
brew upgrade allure
```
------------------------------------------------------------------------

## ▶️ + 📁 allure-results


Запуск всех тестов + Очистка старых результатов:
``` bash
python -m pytest -s -v --alluredir=allure-results --clean-alluredir
```


Открыть временный отчёт:
``` bash
allure serve allure-results
```

------------------------------------------------------------------------

## 📁 ⮕ 🗂️ allure-report


Сгенерировать постоянный отчёт + Очистка старых результатов:
``` bash
allure generate allure-results -o allure-report --clean
```

Открыть готовый отчёт:
``` bash
allure open allure-report
```

------------------------------------------------------------------------

------------------------------------------------------------------------

# @Декораторы

### Заголовок теста (статический)

``` python
@allure.title('Create user')
def test_create_user():
    ...
```
### Заголовок теста (динамический)

``` python
# @allure.title('Create user')  <– ⚠️ статический title - игнорируется при наличии динамического
@pytest.mark.parametrize(       # parametrize 'email' (3-in-1)
    'email', [
        'email_1@amazon.com',
        'email_2gmail.com',
        'email_3yahoo.com'
    ]
)
def test_create_user():
   allure.dynamic.title(f'Create user with Email: {email}')     # 👈 динамический title внутри теста без-@
   ...
```

### Описание теста

``` python
@allure.description('Verify user creation with valid data')
def test_create_user():
    ...
```

### Severity

``` python
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user():
    ...
```

Уровни:

-   BLOCKER
-   CRITICAL
-   NORMAL
-   MINOR
-   TRIVIAL

------------------------------------------------------------------------

### Иерархия

``` python
@allure.epic('API')
@allure.feature('Orders')
@allure.story('Create order')
```

------------------------------------------------------------------------

### Теги

``` python
@allure.tag('smoke')
@allure.tag('regression')
```

------------------------------------------------------------------------

## Issue

``` python
@allure.issue('BUG-123')
```

------------------------------------------------------------------------

## Test Case

``` python
@allure.testcase('TC-456')
```

------------------------------------------------------------------------

# Steps

## Контекстный менеджер

``` python
with allure.step('Create user'):
    ...
```

## Декоратор

``` python
@allure.step('Create user')
def create_user():
    ...
```

С параметрами:

``` python
@allure.step('Create user: {email}')
def create_user(email):
    ...
```

------------------------------------------------------------------------

# Attachments

## JSON

``` python
allure.attach(
    str(response.json()),
    name='Response',
    attachment_type=allure.attachment_type.JSON
)
```

## Screenshot

``` python
allure.attach.file(
    'screenshot.png',
    name='Screenshot',
    attachment_type=allure.attachment_type.PNG
)
```

## Logs

``` python
allure.attach(
    logs,
    name='Logs',
    attachment_type=allure.attachment_type.TEXT
)
```

------------------------------------------------------------------------

# API Testing
## Request Body
``` python
allure.attach(
    str(payload),
    name='Request Body',
    attachment_type=allure.attachment_type.JSON
)
```

## Response Body
``` python
allure.attach(
    response.text,
    name='Response Body',
    attachment_type=allure.attachment_type.JSON
)
```

## Response Headers
``` python
allure.attach(
    str(response.headers),
    name='Response Headers',
    attachment_type=allure.attachment_type.TEXT
)
```

------------------------------------------------------------------------

# Полезные команды
Удаление папок вместе со всем содержимым:
``` bash
rm -rf allure-results
rm -rf allure-report
```

Запустить тесты и открыть отчёт:
``` bash
python -m pytest --alluredir=allure-results
allure serve allure-results
```

------------------------------------------------------------------------

# Вопросы на собеседовании

## В чём разница между `allure serve` и `allure generate`?

-   `allure serve` — временно генерирует отчёт и сразу открывает
    браузер.
-   `allure generate` — создаёт постоянную папку `allure-report`.
-   `allure open` — открывает ранее сгенерированный отчёт `allure-report`.

## Как работает Allure?

``` text
    pytest
      ⬇︎
allure-results  ⮕  allure serve
      ⬇︎        
allure generate
      ⬇︎
 allure open
```

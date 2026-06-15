# Allure Cheat Sheet

## Установка

``` bash
pip install allure-pytest
brew install allure
```

-   **allure-pytest** --- Python-плагин для pytest, который собирает
    результаты тестов в папку `allure-results`.
-   **Allure CLI** --- инструмент для генерации и просмотра
    HTML-отчётов.

------------------------------------------------------------------------

## Запуск тестов с Allure

Запуск всех тестов + Очистка старых результатов:
``` bash
python -m pytest -s -v --alluredir=allure-results --clean-alluredir
```

------------------------------------------------------------------------

## HTML-отчёт

Открыть временный отчёт:
``` bash
allure serve allure-results
```

Сгенерировать постоянный отчёт + Очистка старых результатов:
``` bash
allure generate allure-results -o allure-report --clean
```

Открыть готовый отчёт:
``` bash
allure open allure-report 
```

------------------------------------------------------------------------

## Проверка версии

``` bash
allure --version
```

## Обновление

``` bash
brew upgrade allure
```

------------------------------------------------------------------------

# Декораторы

## Заголовок теста

``` python
@allure.title('Create new user')
def test_create_user():
    ...
```

## Описание теста

``` python
@allure.description('Verify user creation with valid data')
def test_create_user():
    ...
```

## Severity

``` python
@allure.severity(allure.severity_level.CRITICAL)
```

Уровни:

-   BLOCKER
-   CRITICAL
-   NORMAL
-   MINOR
-   TRIVIAL

------------------------------------------------------------------------

## Иерархия

``` python
@allure.epic('API')
@allure.feature('Orders')
@allure.story('Create order')
```

------------------------------------------------------------------------

## Теги

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

-   `allure serve` --- временно генерирует отчёт и сразу открывает
    браузер.
-   `allure generate` --- создаёт постоянную папку `allure-report`.
-   `allure open` --- открывает ранее сгенерированный отчёт.

## Как работает Allure?

``` text
pytest
   ↓
allure-results
   ↓
allure generate / allure serve
   ↓
HTML Report
```

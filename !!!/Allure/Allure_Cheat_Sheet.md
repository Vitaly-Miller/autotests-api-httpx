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
## @Декораторы

### `Tags`

``` python
@allure.tag('SMOKE')
@allure.tag('NEGATIVE')

@allure.tag('SMOKE', 'NEGATIVE')        # Поддерживаетс несколько аннотаций
```

``` python
# Enum:
@allure.tag(Tag.SMOKE)
@allure.tag(Tag.NEGATIVE)

@allure.tag(Tag.SMOKE, Tag.NEGATIVE)    # Поддерживаетс несколько аннотаций
```

------------------------------------------------------------------------
### `Title` - заголовок теста (статический)

``` python
@allure.title('Create user')
def test_create_user():
    ...
```

### `Title` - заголовок теста (динамический)

``` python
@allure.title('Create user')      # <– ⚠️ Статический title - игнорируется при наличии динамического
@pytest.mark.parametrize(           # ┐
    'email', [                      # │
        'email_1@amazon.com',       # │
        'email_2gmail.com',         # │ Pytest parametrize 'email' (3-in-1)
        'email_3yahoo.com'          # │
    ]                               # │
)                                   # ┘
def test_create_user():
   allure.dynamic.title(f'Create user with Email: {email}')     # 👈 Динамический title внутри теста (без-@)
   ...
   
```

------------------------------------------------------------------------
### `Description` - описание теста

``` python
@allure.description('Сreate User with invalid data')
def test_create_user():
    ...
```
------------------------------------------------------------------------
### `Severity` - серьезность

``` python
from allure_commons.types import Severity
#----------------------------------------
@allure.severity(Severity.CRITICAL)
def test_create_user():
    ...
```

`Уровни Severity:`

-   ⚫️️`BLOCKER`
-   🟤`CRITICAL`
-   🔴`NORMAL`
-   🟠`MINOR`
-   🟡`TRIVIAL`

------------------------------------------------------------------------


## Иерархия 
### Behaviors

``` python
@allure.epic('API')             # Epic    — это крупная часть продукта, объединяющая функциональные блоки, которые решают крупные задачи системы. Это уровень самого высокого абстрактного представления, например, проект или модуль в системе.
@allure.feature('Orders')       # Feature — это функциональная возможность продукта, более конкретная, чем epic, но всё ещё широкого охвата. Feature описывает отдельные аспекты системы, такие как конкретные модули или крупные функции.
@allure.story('Create')         # Story   — это конкретный пользовательский сценарий или задача, описывающая конкретные действия, которые может совершать пользователь или система. Story является самой детализированной аннотацией, используемой для описания автотестов.

@allure.story('Create', 'Negative')   # Поддерживается несколько аннотаций
```

``` python
# Enum:
@allure.epic(Epic.API)
@allure.feature(Feature.ORDER)
@allure.story(Story.CREATE)

@allure.story(Story.CREATE, Story.NEGATIVE)   # Поддерживается несколько аннотаций
```

### Suites

``` python
@allure.parent_suite('API')         # = @allure.epic
@allure.suite('Orders')             # = @allure.feature
@allure.sub_suite('Create')         # = @allure.story
```

``` python
# Enum:
@allure.parent_suite(Epic.API)
@allure.suite(Feature.ORDER)
@allure.sub_suite(Story.CREATE)
```
------------------------------------------------------------------------



## Test Case

``` python
@allure.testcase('TC-456')
```

------------------------------------------------------------------------

# Steps

## Контекстный менеджер `with`
— Для описания НЕСКОЛЬКО шагов в функции

``` python
# Test с НЕСКОЛЬКИМИ шагами
def test_step_in_test_with():
    with allure.step('Create User'):        # Описание шага 1 теста (через контекст-менеджер <with>)
        ...                                 # ▶ Actions
    with allure.step('Delete User'):        # Описание шага 2 теста (через контекст-менеджер <with>)
        ...                                 # ▶ Actions
```

``` python
# Функция с ОДНИМ шагом
def get_user():                             # Функция-1
    with allure.step('Get User'):           # Описание шага Функции-1 (через контекст-менеджер <with>)
        ...                                 # ▶ Actions

# Функция с ОДНИМ шагом
def update_user():                          # Функция-2
    with allure.step('Update User'):        # Описание шага Функции-2 (через контекст-менеджер <with>)
        ...                                 # ▶ Actions

#---------------------------
# Test
def test_step_in_func_with():
    get_user()                              # Вызываем Функцию-1 (со встроенным описанием шагов)
    update_user()                           # Вызываем Функцию-2 (со встроенным описанием шагов)


```

## Декоратор `@allure.step()`
— Для описания ОДНОГО/ОБЩЕГО шага

``` python
# Функция с ОДНИМ шагом
@allure.step('Get User')                    # Описание шага Функции-1 (через @декоратор)
def get_user():                             # Функция 1
    ...                                     # ▶ Actions

# Функция с ОДНИМ шагом + ПАРАМЕТР
new_name = 'John Connor'                    # Переменная (параметр)

@allure.step(f'Update User: {new_name}')    # Описание шага Функции-1 (через @декоратор) + параметр
def update_user():                          # Функция 2
    ...                                     # ▶ Actions

#---------------------------------
# Test
def test_step_in_func_decorator():
    get_user()                              # Вызываем Функцию-1 (со встроенным описанием шагов)
    update_user()                           # Вызываем Функцию-2 (со встроенным описанием шагов)

```


## `@allure.step()` + `with`
— Для описания ОБЩЕГО шага функции + ВНУТРЕННИЕ шаги (sub-steps)
``` python
# Функция c ВНУТРЕННИМИ шагами (sub-steps)
@allure.step(f'Build API-Client')               # Описание ОБЩЕГО шага функции (через @декоратор)
def build_api_client():
    with allure.step('Get Auth-token'):         # Описание 1-го внутреннего шага функции (через with)
        ...                                     # ▶ Actions
    with allure.step('Create new API-client'):  # Описание 2-го внутреннего шага функции (через with)
        ...                                     # ▶ Actions

#--------------------------------
# Test
def test_create_file_sub_steps():
    build_api_client()                          # Вызываем Функцию (со встроенным описанием шагов)

```

------------------------------------------------------------------------

## Issue

``` python
@allure.issue('BUG-123')
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

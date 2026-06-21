# Markdown шпаргалка для Python

## 1. Заголовки

```md
# Заголовок 1
## Заголовок 2
### Заголовок 3
#### Заголовок 4
```

Результат:

# Заголовок 1
## Заголовок 2
### Заголовок 3

---

## 2. Выделение текста

```md
**Жирный текст**
*Курсив*
***Жирный курсив***
~~Зачеркнутый текст~~
`inline code`
```

Результат:

**Жирный текст**  
*Курсив*  
***Жирный курсив***  
~~Зачеркнутый текст~~  
`inline code`

> Важно: в обычном Markdown нельзя напрямую менять размер шрифта.  
> Размер обычно зависит от заголовков `#`, `##`, `###` или CSS/HTML, если платформа это поддерживает.

---

## 3. Списки

### Маркированный список

```md
- Python
- Pytest
- Playwright
```

Результат:

- Python
- Pytest
- Playwright

### Нумерованный список

```md
1. Установить зависимости
2. Запустить тесты
3. Проверить отчет
```

Результат:

1. Установить зависимости
2. Запустить тесты
3. Проверить отчет

### Вложенный список

```md
- Tests
  - API tests
  - UI tests
- Reports
  - Allure
  - HTML report
```

Результат:

- Tests
  - API tests
  - UI tests
- Reports
  - Allure
  - HTML report

---

## 4. Блоки кода

### Обычный блок кода

````md
```python
print('Hello, Python!')
```
````

Результат:

```python
print('Hello, Python!')
```

### Пример с Pytest

````md
```python
import pytest

@pytest.mark.parametrize(
    'value, expected',
    [
        (1, 2),
        (2, 4),
        (3, 6),
    ]
)
def test_double(value: int, expected: int):
    assert value * 2 == expected
```
````

Результат:

```python
import pytest

@pytest.mark.parametrize(
    'value, expected',
    [
        (1, 2),
        (2, 4),
        (3, 6),
    ]
)
def test_double(value: int, expected: int):
    assert value * 2 == expected
```

---

## 5. Inline code

Используется для коротких фрагментов кода внутри строки.

```md
Для запуска тестов используй команду `pytest`.
```

Результат:

Для запуска тестов используй команду `pytest`.

---

## 6. Команды терминала

````md
```bash
pip install pytest
pytest -v
```
````

Результат:

```bash
pip install pytest
pytest -v
```

---

## 7. Цитаты

```md
> Это важное замечание.
```

Результат:

> Это важное замечание.

Можно использовать для заметок:

```md
> Note: перед запуском тестов активируй виртуальное окружение.
```

---

## 8. Ссылки

```md
[Официальная документация Python](https://docs.python.org/3/)
```

Результат:

[Официальная документация Python](https://docs.python.org/3/)

---

## 9. Картинки

```md
![Описание картинки](path/to/image.png)
```

Пример:

```md
![Python logo](images/python-logo.png)
```

---

## 10. Таблицы

```md
| Команда | Описание |
|---|---|
| `pytest` | Запустить тесты |
| `pytest -v` | Подробный вывод |
| `pytest -s` | Показывать print |
```

Результат:

| Команда | Описание |
|---|---|
| `pytest` | Запустить тесты |
| `pytest -v` | Подробный вывод |
| `pytest -s` | Показывать print |

---

## 11. Горизонтальная линия

```md
---
```

Результат:

---

Используется для разделения блоков.

---

## 12. Чекбоксы

```md
- [x] Написать тест
- [x] Запустить pytest
- [ ] Проверить Allure отчет
```

Результат:

- [x] Написать тест
- [x] Запустить pytest
- [ ] Проверить Allure отчет

---

## 13. Экранирование символов

Если нужно показать специальный символ Markdown как обычный текст, используй `\`.

```md
\*Это не курсив\*
\# Это не заголовок
```

Результат:

\*Это не курсив\*  
\# Это не заголовок

---

## 14. HTML внутри Markdown

Некоторые платформы поддерживают HTML.

```html
<span style="color:red">Красный текст</span>
<br>
<details>
  <summary>Показать пример</summary>

  Скрытый текст.

</details>
```

> Важно: GitHub поддерживает не весь HTML и почти не поддерживает CSS-стили.

---

## 15. Размер шрифта

В чистом Markdown нет синтаксиса для размера шрифта.

Обычно используют заголовки:

```md
# Большой текст
## Средний текст
### Меньше
```

Или HTML, если платформа разрешает:

```html
<span style="font-size:20px">Текст 20px</span>
```

Но на GitHub такой CSS обычно не работает.

---

## 16. Цвет текста

В чистом Markdown нет цвета текста.

Иногда можно через HTML:

```html
<span style="color:green">Зеленый текст</span>
```

Но на GitHub это обычно не работает.

---

## 17. Скрытый блок details

```md
<details>
  <summary>Показать решение</summary>

```python
def sum_values(a: int, b: int) -> int:
    return a + b
```

</details>
```

Результат:

<details>
  <summary>Показать решение</summary>

```python
def sum_values(a: int, b: int) -> int:
    return a + b
```

</details>

---

## 18. README.md структура для Python-проекта

```md
# Project Name

## Description

Краткое описание проекта.

## Stack

- Python
- Pytest
- Playwright
- Allure

## Installation

```bash
git clone https://github.com/user/project.git
cd project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```bash
pytest
```

## Run tests with Allure

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Project structure

```text
project/
├── tests/
│   └── test_users.py
├── clients/
│   └── user_client.py
├── schemas/
│   └── user_schema.py
├── requirements.txt
└── README.md
```
```

---

## 19. Пример README.md для Pytest + Playwright

````md
# UI Tests

## Stack

- Python
- Pytest
- Playwright

## Installation

```bash
pip install -r requirements.txt
playwright install
```

## Run tests

```bash
pytest
```

## Run specific test

```bash
pytest tests/test_login.py
```

## Run with headed browser

```bash
pytest --headed
```

## Example test

```python
def test_login(page):
    page.goto('https://example.com')
    page.locator('#username').fill('user')
    page.locator('#password').fill('password')
    page.locator('button[type="submit"]').click()

    assert page.locator('h1').inner_text() == 'Dashboard'
```
````

---

## 20. Самые частые конструкции

| Что нужно | Markdown |
|---|---|
| Заголовок | `# Title` |
| Подзаголовок | `## Subtitle` |
| Жирный текст | `**text**` |
| Курсив | `*text*` |
| Код в строке | `` `code` `` |
| Блок Python-кода | ```` ```python ```` |
| Ссылка | `[text](url)` |
| Картинка | `![alt](path)` |
| Таблица | `| A | B |` |
| Цитата | `> text` |
| Чекбокс | `- [ ] task` |
| Горизонтальная линия | `---` |

---

## 21. Полезно для Python-документации

### Хорошо

````md
## Function `create_user`

Создает нового пользователя.

```python
def create_user(name: str, email: str) -> dict:
    return {
        'name': name,
        'email': email,
    }
```

### Parameters

| Name | Type | Description |
|---|---|---|
| `name` | `str` | Имя пользователя |
| `email` | `str` | Email пользователя |

### Returns

| Type | Description |
|---|---|
| `dict` | Данные созданного пользователя |
````

---

## 22. Мини-шаблон для заметок по Python

````md
# Тема

## Кратко

Описание темы в 2-3 предложениях.

## Синтаксис

```python
# пример синтаксиса
```

## Пример

```python
# рабочий пример
```

## Важно запомнить

- Пункт 1
- Пункт 2
- Пункт 3
````

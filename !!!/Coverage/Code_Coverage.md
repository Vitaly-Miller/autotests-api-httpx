# Code Coverage (Покрытие кода)

---
### 1. Установка библиотеки (модуля)
```shell
pip install coverage
```
---
### 2. Запуск тестов с измерением покрытия
- Запуск всех тестов
```shell
coverage run -m pytest -s -v
```

- Запуск тестов по маркировке
```shell
coverage run -m pytest -m "regression"
```
---
### 3. Генерация HTML отчёта

```shell
coverage html
```
---

### 4. Открытие HTML отчёта
В результате будет создана папка 📁`htmlcov`, в которой появится файл `index.html`

---

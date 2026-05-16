"""
@pytest.mark.usefixtures()
Позволяет использовать НЕСКОЛЬКО ФИКСТУР без явной передачи их в качестве параметра теста/функции.
⚠️Использовать только для логики, т.к. нет доступа к return этой фикстуры.
⚠️Если нужно использовать данные из return - использовать обычный способ (в качестве передаваемого аргумента функции).
"""
import pytest

#=======================================================================================================================
# Фикстуры:
@pytest.fixture
def clear_books_database():
    print('[FIXTURE] 🚫Clear')

@pytest.fixture
def fill_books_database():
    print('[FIXTURE] ✅Fill')



# Классический способ применения фикстур (передача фикстуры в качестве аргумента тест-функции)
class TestLibrary1:
    def test_read_book_from_library(self, fill_books_database, clear_books_database):
        ...

    def test_delete_books_database(self, fill_books_database, clear_books_database):
        ...


# @pytest.mark.usefixtures() - для .методов класса (тест-функций)
class TestLibrary2:
    @pytest.mark.usefixtures('fill_books_database', 'clear_books_database')
    def test_read_book_from_library(self):
        ...

    @pytest.mark.usefixtures('fill_books_database', 'clear_books_database')
    def test_delete_books_database(self):
        ...


# @pytest.mark.usefixtures() - для класса - применится ко всем .методам класса (тест-функцииям)
@pytest.mark.usefixtures('fill_books_database', 'clear_books_database')
class TestLibrary3:
    def test_read_book_from_library(self):
        ...

    def test_delete_books_database(self):
        ...

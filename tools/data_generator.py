"""
Data Generator
"""
from faker import Faker

#=======================================================================================================================
class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    #-------------------------------------------------------------------------------------------------------------------
    def first_name(self) -> str:
        """
        Генерация First Name

        :return: John
        """
        return self.faker.first_name()

    #-------------------------------------------------------------------------------------------------------------------
    def middle_name(self) -> str:
        """
        Генерация Middle Name

        :return: Connor
        """
        return self.faker.first_name()

    #-------------------------------------------------------------------------------------------------------------------
    def last_name(self) -> str:
        """
        Генерация Last Name

        :return: Connor
        """
        return self.faker.last_name()

    #-------------------------------------------------------------------------------------------------------------------
    def email(self) -> str:
        """
        Генерация email

        :return: example@example.com
        """
        return self.faker.email()

    #-------------------------------------------------------------------------------------------------------------------
    def password(self) -> str:
        """
        Генерация пароля

        :return: Password
        """
        return self.faker.password()

    #-------------------------------------------------------------------------------------------------------------------
    def user_id(self) -> str:
        """
        Генерация бизнес-формата User ID

        :return: USER-12345
        """
        number = self.faker.random_int(10000, 99999)
        return f'USER-{number}'

    #-------------------------------------------------------------------------------------------------------------------
    def uuid4(self) -> str:
        """
        Генерация UUID

        :return: <cad77163-f85d-4b96-b807-27670ffc9c29>
        """
        return self.faker.uuid4()

    #-------------------------------------------------------------------------------------------------------------------
    def text(self, max_nb_chars: int = 100) -> str:
        """
        Генерация текста с заданной максимальной длиной.

        :param max_nb_chars: Максимальная длина (в символах). Default = 100
        :return: Случайные предложения
        """
        return self.faker.text(max_nb_chars=max_nb_chars)

    #-------------------------------------------------------------------------------------------------------------------
    def estimated_time(self, minimum: int = 2, maximum: int = 9) -> str:
        """
        Генерация оценочного времени в неделях. Default = [2-9]

        :return: [2-9] weeks
        """
        quantity = self.faker.random_int(minimum, maximum)
        return f'{quantity} weeks'

    #-------------------------------------------------------------------------------------------------------------------
    def max_core(self) -> int:
        """
        Генерация Max Score

        :return: [50-100]
        """
        return self.faker.random_int(50, 100)

    #-------------------------------------------------------------------------------------------------------------------
    def min_score(self) -> int:
        """
        Генерация Min Score

        :return: [1-30]
        """
        return self.faker.random_int(1, 30)


# Экземпляр класса
fake = Fake(faker=Faker())


print(fake.first_name())
print(fake.middle_name())
print(fake.last_name())
print(fake.email())
print(fake.password())
print(fake.user_id())
print(fake.uuid4())
print(fake.text())
print(fake.text(max_nb_chars=500))
print(fake.estimated_time())
print(fake.max_core())
print(fake.min_score())


#=======================================================================================================================
# Инициализация (Экземпляр класса)
fake = Faker()

#------------------------------------------------- User Credentials  ---------------------------------------------------
# User email
def generate_email() -> str:
    return fake.email()

# User password
def generate_password() -> str:
    return fake.password()

#===================================================== faker Examples ========================================================
print(f'Full Name            |  {fake.name()}')
print(f'Free email           |  {fake.free_email()}')
print(f'Company email        |  {fake.company_email()}')
# Цифры
print(f'Digits  (0 to 9)     |  {fake.random_digit()}')
print(f'Digits  (100 to 999) |  {fake.random_int(min=100, max=999)}')
print(f'Numeric ID (4-dig)   |  {fake.pyint()}')
# Токены
print(f'sha256               |  {fake.sha256()}')   # 9d383ef1c2b1b90990b1571f89a3c808afce0d56f5815a0394ec625fdd6908cf
print(f'md5                  |  {fake.md5()}')      # 1a31f9244b06f85b51c66fd21c38d6c7
print(f'UUID                 |  {fake.uuid4()}')    # cad77163-f85d-4b96-b807-27670ffc9c29
# Строки
print(f'Текст               |   {fake.text()}')     # Such drop give top generation across. American democratic similar student Mr always. Heart business same itself talk set. Push threat amount wish picture peace lay. Certainly modern should could.
print(f'Буквы                |  {fake.lexify(text='Id-??????')}')     # Id-aDhLqx
print(f'Цифры                |  {fake.numerify(text='Id-######')}')   # Id-786444
print(f'Буквы + Цифры        |  {fake.bothify(text='Id-???###')}')    # Id-DgO817

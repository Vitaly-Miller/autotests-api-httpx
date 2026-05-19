"""
Модуль (библиотека) Faker()
"""
from faker import Faker

#========================================================  ℹ️ ==========================================================
fake = Faker()

# Credentials
print(f'First name                |  {fake.first_name()}')
print(f'Last name                 |  {fake.last_name()}')
print(f'Full name                 |  {fake.name()}')
print(f'Free email                |  {fake.free_email()}')

print(f'Email                     |  {fake.email()}')
print(f'Email (Domain)            |  {fake.email(domain="amazon.com")}')
print(f'Email (Company)           |  {fake.company_email()}')

# Цифры
print(f'Digits  (0 to 9)          |  {fake.random_digit()}')
print(f'Digits  (4 digits)        |  {fake.random_int()}')
print(f'Digits  (100 to 999)      |  {fake.random_int(min=100, max=999)}')


print(f'Numeric ID (4-dig)        |  {fake.pyint()}')

# Токены
print(f'sha256                    |  {fake.sha256()}')    # 9d383ef1c2b1b90990b1571f89a3c808afce0d56f5815a0394ec625fdd6908cf
print(f'md5                       |  {fake.md5()}')       # 1a31f9244b06f85b51c66fd21c38d6c7
print(f'UUID                      |  {fake.uuid4()}')     # cad77163-f85d-4b96-b807-27670ffc9c29
print(f'UUID (без "-")            |  {fake.uuid4().replace('-', '')}')    # cad77163f85d4b96b80727670ffc9c29
print(f'UUID (короткий)           |  {fake.uuid4()[:8]}')  # cad77163

# Текст
print(f'Текст                     |  {fake.text()}')
print(f'Текст (<50 chars)         |  {fake.text(max_nb_chars=50)}')
print(f'Предложение (6 words)     |  {fake.sentence()}')

# Буквы
print(f'Буквы (4 chars)           |  {fake.lexify()}')                     # ZPHq
print(f'Буквы (custom)            |  {fake.lexify(text='Id-??????')}')     # Id-ajhPqx

# Цифры
print(f'Цифры (3 chars)           |  {fake.numerify()}')                   # 461
print(f'Цифры (custom)            |  {fake.numerify(text='Id-######')}')   # Id-786444

# Буквы + Цифры
print(f'Буквы + Цифры (2+2 chars) |  {fake.bothify()}')                    # 28 Wf
print(f'Буквы + Цифры (custom)    |  {fake.bothify(text='Id-???###')}')    # Id-dGu817

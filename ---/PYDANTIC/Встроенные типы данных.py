"""
Pydantic встроенные типы данных
HttpUrl  -  (⚠️БЕСПОЛЕЗНАЯ ШТУКА) - Проверяет только http или https
EmailStr -  (✅НОРМ)              - Проверяет email полностью
"""

from pydantic import BaseModel, HttpUrl, EmailStr

#=======================================================================================================================
class CompanySchema(BaseModel):         # Основная схема
    url: HttpUrl
    email: EmailStr


company = CompanySchema(
    url='https://website.com',           # НЕ ОШИБКА! -> Можно url=HttpUrl('https://website.com') - чтоб IDE не ругался
    email='info@email.com'
)

print(company)                           # url=HttpUrl('https://website.com/') email='info@email.com'
print(company.model_dump())              # {'url': HttpUrl('https://website.com/'), 'email': 'info@email.com'}
print(company.model_dump(mode='json'))   # {'url': 'https://website.com/', 'email': 'info@email.com'}   ✨- убрал HttpUrl
print(company.model_dump_json())         # {"url":"https://website.com/","email":"info@email.com"}


print(type(company.email))  # str
print(type(company.url))    # HttpUrl

print(company.url.scheme)   # https
print(company.url.host)     # website.com
print(company.url.path)     # /
#=======================================================================================================================

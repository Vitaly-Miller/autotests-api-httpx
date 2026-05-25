"""
Test Get User Me 0
"""
"""
- Без фикстур (Manual)
"""
from http import HTTPMethod, HTTPStatus
import jsonschema
import pytest
from schemas.auth import AuthUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from schemas.users import CreateUserRequestSchema, CreateUserResponseSchema

#=======================================================================================================================
@pytest.mark.smoke            # маркировка smoke
@pytest.mark.users            # маркировка users
def test_get_user_me():
    #------------------------------------------------- Pre-conditions --------------------------------------------------
    # Create User
    public_users_client = get_public_users_client()       # Получаем экземпляр PublicUsersClient c уже настроенным HTTP-клиентом с Base URL
    create_user_data = CreateUserRequestSchema()          # Инициализация Pydantic-модели с генерацией fake User data нового пользователя для регистрации

    public_users_client.create_user(create_user_data=create_user_data) # ▶ Запрос на создание пользователя

    auth_data = AuthUserSchema(                 # Инициализируем модель с данными для авторизации
        email=create_user_data.email,           # Вытаскиваем .Email из модели
        password=create_user_data.password)     # Вытаскиваем .Password из модели


    #--------------------------------------------------- Get User Me ---------------------------------------------------
    get_user_me_client = get_private_users_client(auth_data)   # Получаем экземпляр PrivateUsersClient c уже настроенным HTTP-клиентом с Base URL
    response = get_user_me_client.get_user_me_api()            # ▶ Запрос на получение данных ТЕКУЩЕГО пользователя через API-метод

    response_model = CreateUserResponseSchema.model_validate_json(response.text)  # JSON-ответ —> Pydantic-model (десериализация для Assertions)


    #-------------------------------------------- Assertions (классический) --------------------------------------------
    # Base API assertions (⚠️Hard coding не рекомендуется)
    assert response.status_code == 200, '❌Status code is incorrect!'             # проверка статус-кода    (Hard coding)
    assert response.request.method == 'GET', '❌Request Method is incorrect!'     # проверка метода запроса (Hard coding)

    # Base API assertions (через HTTPStatus и HTTPMethod)
    assert response.status_code == HTTPStatus.OK, '❌Incorrect status code!'             # проверка статус-кода    (через HTTPStatus)
    assert response.request.method == HTTPMethod.GET, '❌Incorrect Request Method!'      # проверка метода запроса (через HTTPMethod)

    # Fields values assertions
    assert response_model.user.email == create_user_data.email, '❌Разные Email!'                    # проверка отправленного и полученного Email
    assert response_model.user.last_name == create_user_data.last_name, '❌Разные Last Name!'        # проверка отправленного и полученного Last Name
    assert response_model.user.first_name == create_user_data.first_name, '❌Разные First Name!'     # проверка отправленного и полученного First Name
    assert response_model.user.middle_name == create_user_data.middle_name, '❌Разные Middle Name!'  # проверка отправленного и полученного Middle Name

    # Validation JSON Schema
    jsonschema.validate(
        instance=response.json(),                             # Данные для валидации в формате JSON
        schema=CreateUserResponseSchema.model_json_schema(),  # JSON-схема, сгенерированная из Pidantic-схемы
        format_checker=jsonschema.FormatChecker()             # Проверка форматов
    )

#=======================================================================================================================

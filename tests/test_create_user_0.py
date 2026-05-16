"""
Test Create User 0
(Manual) Без фикстур
"""
import jsonschema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus, HTTPMethod

#=======================================================================================================================
def test_create_user():
    public_users_client = get_public_users_client()   # Инициализация клиента (public). Создает экземпляр класса PublicUsersClient
    create_user_data = CreateUserRequestSchema()      # Инициализация модели с fake данными нового пользователя по Pydantic-схеме

    # ▶ Запрос на создание пользователя через API-метод
    response = public_users_client.create_user_api(create_user_data=create_user_data)          # Передаем сгенерированные в Pydantic-схеме fake данные нового пользователя

    # JSON-ответ —> Pydantic модель (десериализация для Assertions)
    response_model = CreateUserResponseSchema.model_validate_json(response.text)


    #-------------------------------------------- Assertions (классический) --------------------------------------------
    assert response.status_code == 200           # проверка статус-кода    (⚠️Hard coding не рекомендуется)
    assert response.request.method == 'POST'     # проверка метода запроса (⚠️Hard coding не рекомендуется)

    assert response.status_code == HTTPStatus.OK, '❌Incorrect status code!'             # проверка статус-кода (через HTTPStatus)
    assert response.request.method == HTTPMethod.POST, '❌Incorrect Request Method!'     # проверка метода запроса (через HTTPMethod)

    assert response_model.user.email == create_user_data.email, '❌Разные Email!'                    # проверка отправленного и полученного email
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

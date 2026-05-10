"""
сonftest.py
Хранение фикстур
"""
import pytest
from pydantic import BaseModel
from clients.auth.auth_client import get_auth_client, AuthClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

#=======================================================================================================================
#-------------------------------------------- Инициализация client (public) --------------------------------------------
@pytest.fixture                                     # Default scope='function'
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

#------------------------------------------------ Authentication client ------------------------------------------------
@pytest.fixture                                     # Default scope='function'
def auth_client() -> AuthClient:
    return get_auth_client()

#--------------------------------------------- Function User (Create User) ✨-------------------------------------------
# Схема для объединения данных пользователя (Request + Response)                                                         # ⚠️Решить о переносе схемы в users_schema
class UserFullSchema(BaseModel):
    """
    Объединенные данные о пользователе из Request и Response в формате Pydantic-model

    Request  -> Данные о пользователе (первичные)
    Response -> Данные о пользователе (первичные, КРОМЕ password) + User ID и еще...
    """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    # Оперативные данные (что бы быстро достать)
    @property
    def email(self) -> str:
        return self.request.email            # Email

    @property
    def password(self) -> str:
        return self.request.password         # Password

    @property
    def user_id(self) -> str:
        return self.response.user.id         # User ID


# Function User (Create User)
@pytest.fixture                                                                 # Default scope='function'
def function_user(public_users_client: PublicUsersClient) -> UserFullSchema:    # Вложенная фикстура: c аннотацией (<function_> в названии функции - это scope='function' - для удобства понимания при использовании)
    create_user_payload = CreateUserRequestSchema()                             # Инициализация модели с fake-данными нового пользователя по Pydantic-схеме
    response = public_users_client.create_user(payload=create_user_payload)     # ︎▶ Запрос на создание пользователя через .метод. Передаем сгенерированные в Pydantic-схеме fake-данные нового пользователя
    return UserFullSchema(request=create_user_payload, response=response)       # Возвращает Pydantic-model с объединенными данные о пользователе (Request + Response)

#-----------------------------------------------------------------------------------------------------------------------

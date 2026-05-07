"""
PUBLIC Users Client
/users
(Для методов, НЕ требующих авторизации)
"""
from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

#======================================================= Client ========================================================
class PublicUsersClient(APIClient):
    ENDPOINT = '/users'
    #------------------------------------------------- Create User  ----------------------------------------------------
    def create_user_api(self, payload: CreateUserRequestSchema) -> Response:
        """
        Метод для СОЗДАНИЯ нового пользователя

        :param payload: Данные для создания пользователя в формате Pydantic-модели
        :return: httpx.Response
        """
        return self.post(
            url=self.ENDPOINT,
            json=payload.model_dump(by_alias=True))  # ⚠ сериализация Model —> Dict (т.к. в payload передаем Pydantic-модель) + 🐫CamelCase

    def create_user(self, payload: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Метод для СОЗДАНИЯ нового пользователя с получением данных созданного пользователя в формате Pydantic-model.

        :param payload: Данные для создания нового пользователя в формате Pydantic-модели
        :return: Данные созданного пользователя в формате Pydantic-model
        """
        response = self.create_user_api(payload)                            # Используем API-метод создания нового пользователя
        return CreateUserResponseSchema.model_validate_json(response.text)  # Валидируем ответ (любой) —> Model


#=============================================== Client Builder (Public) ===============================================
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом

    :return: Готовый к использованию PrivateUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())

#-----------------------------------------------------------------------------------------------------------------------

"""
PUBLIC Users Client
/users
(Для методов, НЕ требующих авторизации)
"""
import httpx
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

#================================================= Public Users Client =================================================
class PublicUsersClient(APIClient):
    ENDPOINT = '/users'
    #------------------------------------------------- Create User  ----------------------------------------------------
    # API 🟨
    def create_user_api(self, create_user_data: CreateUserRequestSchema) -> httpx.Response:
        """
        Метод для СОЗДАНИЯ нового пользователя

        :param create_user_data: (payload) Данные для создания пользователя в формате Pydantic-модели
        :return: httpx.Response
        """
        return self.post(
            url=self.ENDPOINT,
            json=create_user_data.model_dump(by_alias=True))                # Serialize Model —> Dict

    # Pydantic-model
    def create_user(self, create_user_data: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Метод для СОЗДАНИЯ нового пользователя с получением данных созданного пользователя в формате Pydantic-model

        :param create_user_data: (payload) Данные для создания нового пользователя в формате Pydantic-модели
        :return: Данные созданного пользователя в формате Pydantic-model
        """
        response = self.create_user_api(create_user_data)                   # Используем API-метод
        return CreateUserResponseSchema.model_validate_json(response.text)  # Валидируем ответ (любой) —> Model


#================================================= Client (✨Helper) ===================================================
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр класса PrivateUsersClient с уже настроенным HTTP-клиентом

    :return: Готовый к использованию экземпляр класса PrivateUsersClient с уже настроенным HTTP-клиентом
    """
    return PublicUsersClient(client=get_public_http_client())

#-----------------------------------------------------------------------------------------------------------------------

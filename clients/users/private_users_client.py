"""
🔒PRIVATE Users Client
/users
(Для методов, требующих авторизации)
"""
import httpx
from clients.api_client import APIClient
from clients.auth.auth_schema import AuthUserSchema
from clients.private_http_builder import get_private_http_client
from clients.users.users_schema import (
    UpdateUserRequestSchema,
    GetUserResponseSchema,
    GetUserMeResponseSchema,
    UserUpdateResponseSchema
)

#================================================ Private Users Client =================================================
class PrivateUsersClient(APIClient):
    ENDPOINT = '/users'
    #------------------------------------------------- Get User Me -----------------------------------------------------
    # API 🟩
    def get_user_me_api(self) -> httpx.Response:
        """
        Метод ПОЛУЧЕНИЯ данных ТЕКУЩЕГО пользователя

        :return: httpx.Response
        """
        return self.get(url=f'{self.ENDPOINT}/me')

    # Pydantic-model
    def get_user_me(self) -> GetUserMeResponseSchema:
        """
        Метод ПОЛУЧЕНИЯ данных ТЕКУЩЕГО пользователя в формате Pydantic-model

        :return: Pydantic-model: GetUserMeResponseSchema
        """
        response = self.get_user_me_api()                                     # Используем API-метод для запроса
        return GetUserMeResponseSchema.model_validate_json(response.text)     # Валидируем ответ (любой) —> Model


    #-------------------------------------------------- Get User -------------------------------------------------------
    # API 🟩
    def get_user_api(self, user_id: str) -> httpx.Response:
        """
        Метод для ПОЛУЧЕНИЯ данных пользователя по User ID

        :param user_id: User ID
        :return: httpx.Response
        """
        return self.get(url=f'{self.ENDPOINT}/{user_id}')

    # Pydantic-model
    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод для ПОЛУЧЕНИЯ данных пользователя по User ID в формате Pydantic-модели

        :param user_id: User ID
        :return: Ответ с данными конкретного пользователя в формате Pydantic-model
        """
        response = self.get_user_api(user_id)                                 # Используем API-метод для запроса
        return GetUserResponseSchema.model_validate_json(response.text)       # Валидируем ответ (любой) —> Model


    #------------------------------------------------- Update User -----------------------------------------------------
    # API 🟪
    def update_user_api(self, user_id: str, update_data: UpdateUserRequestSchema) -> httpx.Response:
        """
        Метод для ЧАСТИЧНОГО ОБНОВЛЕНИЯ данных пользователя по User ID

        :param user_id: User ID
        :param update_data: Данные: email, firstName, middleName, lastName - в формате Pydantic-model
        :return: httpx.Response
        """
        return self.patch(
            url=f'{self.ENDPOINT}/{user_id}',
            json=update_data.model_dump(by_alias=True)                        # Serialize Model —> Dict
        )

    # Pydantic-model
    def update_user(self, user_id: str, payload: UpdateUserRequestSchema) -> UserUpdateResponseSchema:
        """
        Метод для ЧАСТИЧНОГО ОБНОВЛЕНИЯ данных пользователя по User ID

        :param user_id: User ID
        :param payload: Данные: email, firstName, middleName, lastName - в формате Pydantic-model
        :return: httpx.Response
        """
        response = self.update_user_api(user_id, payload)   # Используем API-метод для запроса
        return UserUpdateResponseSchema.model_validate_json(response.text)    # Валидируем ответ (любой) —> Model


    #------------------------------------------------- Delete User -----------------------------------------------------
    # API 🟥
    def delete_user_api(self, user_id: str) -> httpx.Response:
        """
        Метод для УДАЛЕНИЯ пользователя по User ID

        :param user_id: User ID
        :return: httpx.Response
        """
        return self.delete(url=f'{self.ENDPOINT}/{user_id}')

    # Pydantic-model (⚠️Дописать)
    def delete_user(self, user_id: str) -> None:
        ...

#================================================= Client (✨Helper) ===================================================
def get_private_users_client(auth_data: AuthUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом (Base URL + Auth)

    :param auth_data: Данные для аутентификации пользователя (Email, Password) в формате Pydantic-model
    :return: Готовый к использованию PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(auth_data))

#-----------------------------------------------------------------------------------------------------------------------

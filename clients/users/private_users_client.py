"""
🔒PRIVATE Users Client
/users
(Для методов, требующих авторизации)
"""
from httpx import Response
from clients.api_client import APIClient
from clients.auth.auth_schema import AuthUserSchema
from clients.private_http_builder import get_private_http_client
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema

#======================================================= Client ========================================================
class PrivateUsersClient(APIClient):
    ENDPOINT = '/users'
    #------------------------------------------------- Get User Me -----------------------------------------------------
    def get_user_me_api(self) -> Response:
        """
        Метод ПОЛУЧЕНИЯ данных ТЕКУЩЕГО пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'{self.ENDPOINT}/me')

    #-------------------------------------------------- Get User -------------------------------------------------------
    def get_user_api(self, user_id: str) -> Response:
        """
        Метод для ПОЛУЧЕНИЯ данных конкретного пользователя.

        :param user_id: User ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'{self.ENDPOINT}/{user_id}')

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод получения Pydantic-модели/JSON-объекта с данными конкретного пользователя.

        :param user_id: User ID
        :return: Pydantic-модель с данными пользователя по User ID
        :return: JSON-объект с данными пользователя по User ID
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)  # ⚠ <- Валидируем ответ (любой) -> Model
        return response.json()                                           # ⚠ <- Может вызвать ошибку, если придет не JSON


    #------------------------------------------------- Update User -----------------------------------------------------
    def update_user_api(self, user_id: str, payload: UpdateUserRequestSchema) -> Response:
        """
        Метод для ЧАСТИЧНОГО ОБНОВЛЕНИЯ данных пользователя по User ID.

        :param user_id: User ID
        :param payload: Словарь с email, firstName, middleName, lastName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            url=f'{self.ENDPOINT}/{user_id}',
            json=payload.model_dump(by_alias=True)    # + ⚠ сериализация Model -> Dict (т.к. payload - Pydantic-модель)
        )

    #------------------------------------------------- Delete User -----------------------------------------------------
    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод для УДАЛЕНИЯ пользователя по User ID.

        :param user_id: User ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{self.ENDPOINT}/{user_id}')


#================================================ Client Builder (Private) =============================================
def get_private_users_client(auth_data: AuthUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :param auth_data: Данные для аутентификации пользователя (Email, Password)
    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(auth_data))

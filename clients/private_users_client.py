"""
🔒Private Users Client
(Для методов, требующих авторизации)
/users
"""
import httpx
from clients.api_client import APIClient
from schemas.auth import AuthUserSchema
from clients.httpx_private_client import get_httpx_private_client
from schemas.users import (
    UpdateUserRequestSchema,
    GetUserResponseSchema,
    GetUserMeResponseSchema,
    UserUpdateResponseSchema
)

#================================================ Private Users Client =================================================
class PrivateUsersClient(APIClient):
    ENDPOINT = '/users'
    #------------------------------------------------- Get User Me -----------------------------------------------------
    # API
    def get_user_me_api(self) -> httpx.Response:
        """
        API-метод получения данных текущего пользователя

        :return: httpx.Response
        """
        response = self.get(url=f'{self.ENDPOINT}/me')                         # ▶ Запрос
        return response                                                        # httpx.Response

    # Pydantic-model
    def get_user_me(self) -> GetUserMeResponseSchema:
        """
        Pydantic-метод получения данных текущего пользователя

        :return: Pydantic-model (GetUserMeResponseSchema)
        """
        response = self.get_user_me_api()                                      # ▶ Запрос через API-метод
        model = GetUserMeResponseSchema.model_validate_json(response.text)     # Response —> Pydantic-model (deserialize)
        return model


    #-------------------------------------------------- Get User -------------------------------------------------------
    # API
    def get_user_api(self, user_id: str) -> httpx.Response:
        """
        API-метод получения данных пользователя по User ID

        :param user_id: User ID
        :return: httpx.Response
        """
        response = self.get(url=f'{self.ENDPOINT}/{user_id}')                  # ▶ Запрос
        return response                                                        # httpx.Response

    # Pydantic-model
    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Pydantic-метод получения данных пользователя по User ID

        :param user_id: User ID
        :return: Pydantic-model (GetUserResponseSchema)
        """
        response = self.get_user_api(user_id)                                  # ▶ Запрос через API-метод
        model = GetUserResponseSchema.model_validate_json(response.text)       # Response —> Pydantic-model (deserialize)
        return model


    #------------------------------------------------- Update User -----------------------------------------------------
    # API
    def update_user_api(self, user_id: str, update_data: UpdateUserRequestSchema) -> httpx.Response:
        """
        API-метод частичного обновления данных пользователя по User ID

        :param user_id: User ID
        :param update_data: Pydantic-model c данными, которые необходимо обновить
        :return: httpx.Response
        """
        response = self.patch(                                                 # ▶ Запрос
            url=f'{self.ENDPOINT}/{user_id}',
            json=update_data.model_dump(by_alias=True)                         # Pydantic-model —> Dict (serialize)
        )
        return response                                                        # httpx.Response

    # Pydantic-model
    def update_user(self, user_id: str, update_data: UpdateUserRequestSchema) -> UserUpdateResponseSchema:
        """
        Pydantic-метод частичного обновления данных пользователя по User ID

        :param user_id: User ID
        :param update_data: Pydantic-model c данными, которые необходимо обновить
        :return: Pydantic-model (UserUpdateResponseSchema)
        """
        response = self.update_user_api(user_id, update_data)  # ▶ Запрос через API-метод
        model = UserUpdateResponseSchema.model_validate_json(response.text)      # Response —> Pydantic-model (deserialize)
        return model                                                             # Pydantic-model (UserUpdateResponseSchema)


    #------------------------------------------------- Delete User -----------------------------------------------------
    # API
    def delete_user_api(self, user_id: str) -> httpx.Response:
        """
        API-метод удаления пользователя по User ID

        :param user_id: User ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{self.ENDPOINT}/{user_id}')              # ▶ Запрос
        return response                                                       # httpx.Response

    # Pydantic-model (⚠️Дописать Схему)
    # def delete_user(self, user_id: str) -> DeleteUserResponseSchema:
    #     """
    #     Pydantic-метод удаления пользователя по User ID
    #
    #     :param user_id: User ID
    #     :return: Pydantic-model (DeleteUserResponseSchem)
    #     """
    #     response = self.delete_user_api(user_id)                             # ▶ Запрос через API-метод
    #     model = DeleteUserResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (deserialize)
    #     return model                                                         # Pydantic-model (DeleteUserResponseSchem)


#================================================= Client (✨Helper) ===================================================
def get_private_users_client(auth_data: AuthUserSchema) -> PrivateUsersClient:
    """
    Функция получения экземпляра PrivateUsersClient с уже настроенным HTTP-клиентом (с Авторизацией)

    :param auth_data: Pydantic-model с данными для аутентификации пользователя (Email, Password)
    :return: Экземпляр PrivateUsersClient
    """
    private_users_client = PrivateUsersClient(client=get_httpx_private_client(auth_data))
    return private_users_client

#-----------------------------------------------------------------------------------------------------------------------

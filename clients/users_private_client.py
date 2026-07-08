"""
Users Client (🔒Private)
(Для методов, требующих авторизации)
"""
import httpx
import allure
from clients.api_client import APIClient
from schemas.auth_schema import AuthDataSchema
from clients.httpx_private_client import get_httpx_private_client
from schemas.users_schema import (
    UpdateUserRequestSchema,
    GetUserResponseSchema,
    GetUserMeResponseSchema,
    UserUpdateResponseSchema
)

#============================================== Users Client (🔒Private) ===============================================
class PrivateUsersClient(APIClient):
    ENDPOINT = '/api/v1/users'
    #------------------------------------------------- Get User Me -----------------------------------------------------
    # API
    @allure.step('▶ Get User Me')
    def get_user_me_api(self) -> httpx.Response:
        """
        API-метод получения данных текущего пользователя

        :return: httpx.Response
        """
        response = self.get(url=f'{self.ENDPOINT}/me')                               # ▶ Запрос
        return response                                                              # httpx.Response


    # Pydantic-model
    @allure.step('▶ Get User Me (Pydantic)')
    def get_user_me(self) -> GetUserMeResponseSchema:
        """
        Pydantic-метод получения данных текущего пользователя

        :return: Pydantic-model (GetUserMeResponseSchema)
        """
        response = self.get_user_me_api()                                             # ▶ Запрос через API-метод
        response_model = GetUserMeResponseSchema.model_validate_json(response.text)   # httpx.Response —> Pydantic-model (parsing-deserialize) (deserialize)
        return response_model                                                         # Pydantic-model (GetUserMeResponseSchema)


    #-------------------------------------------------- Get User -------------------------------------------------------
    # API
    @allure.step('▶ Get User by ID (API)')
    def get_user_api(self, user_id: str) -> httpx.Response:
        """
        API-метод получения данных пользователя по User-ID

        :param user_id: User-ID
        :return: httpx.Response
        """
        response = self.get(url=f'{self.ENDPOINT}/{user_id}')        # ▶ Запрос
        return response                                              # httpx.Response


    # Pydantic-model
    @allure.step('▶ Get User by ID (Pydantic)')
    def get_user_pydantic(self, user_id: str) -> GetUserResponseSchema:
        """
        Pydantic-метод получения данных пользователя по User-ID

        :param user_id: User-ID
        :return: Pydantic-model (GetUserResponseSchema)
        """
        response = self.get_user_api(user_id)                                        # ▶ Запрос через API-метод
        response_model = GetUserResponseSchema.model_validate_json(response.text)    # httpx.Response —> Pydantic-model (parsing-deserialize) (deserialize)
        return response_model                                                        # Pydantic-model (GetUserResponseSchema)


    #------------------------------------------------- Update User -----------------------------------------------------
    # API
    @allure.step('▶ Update User by ID (API)')
    def update_user_api(self, user_id: str, update_data: UpdateUserRequestSchema) -> httpx.Response:
        """
        API-метод частичного обновления данных пользователя по User-ID

        :param user_id: User-ID
        :param update_data: Pydantic-model c данными, которые необходимо обновить
        :return: httpx.Response
        """
        response = self.patch(                                      # ▶ Запрос
            url=f'{self.ENDPOINT}/{user_id}',
            json=update_data.model_dump(by_alias=True)              # Pydantic-model —> Dict (serialize)
        )
        return response                                             # httpx.Response


    # Pydantic-model
    @allure.step('▶ Update User by ID (Pydantic)')
    def update_user_pydantic(self, user_id: str, update_data: UpdateUserRequestSchema) -> UserUpdateResponseSchema:
        """
        Pydantic-метод частичного обновления данных пользователя по User-ID

        :param user_id: User-ID
        :param update_data: Pydantic-model c данными, которые необходимо обновить
        :return: Pydantic-model (UserUpdateResponseSchema)
        """
        response = self.update_user_api(user_id, update_data)         # ▶ Запрос через API-метод
        response_model = UserUpdateResponseSchema.model_validate_json(response.text)    # httpx.Response —> Pydantic-model (parsing-deserialize) (deserialize)
        return response_model                                                           # Pydantic-model (UserUpdateResponseSchema)


    #------------------------------------------------- Delete User -----------------------------------------------------
    # API
    @allure.step('▶ Delete User by ID (API)')
    def delete_user_api(self, user_id: str) -> httpx.Response:
        """
        API-метод удаления пользователя по User-ID

        :param user_id: User-ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{self.ENDPOINT}/{user_id}')    # ▶ Запрос
        return response                                             # httpx.Response


#=================================================== Client (Helper) ===================================================
@allure.step('◎ Get Users Client (Private)')
def get_private_users_client(auth_data: AuthDataSchema) -> PrivateUsersClient:
    """
    Функция получения экземпляра PrivateUsersClient() с уже настроенным httpx.Client (Private)

    :param auth_data: Pydantic-model с данными для аутентификации пользователя (Email, Password)
    :return: Настроенный экземпляр PrivateUsersClient()
    """
    private_users_client = PrivateUsersClient(client=get_httpx_private_client(auth_data))
    return private_users_client                                                        # PrivateUsersClient()

#-----------------------------------------------------------------------------------------------------------------------

"""
PUBLIC Users Client
(Для методов, НЕ требующих авторизации)
"""
import httpx
import allure
from clients.api_client import APIClient
from clients.httpx_public_client import get_httpx_public_client
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

#================================================= Public Users Client =================================================
class PublicUsersClient(APIClient):
    ENDPOINT = '/users'
    #------------------------------------------------- Create User  ----------------------------------------------------
    # API
    @allure.step('Create user (API)')
    def create_user_api(self, create_user_data: CreateUserRequestSchema) -> httpx.Response:
        """
        API-метод создания нового пользователя

        :param create_user_data: Pydantic-model c данными для создания пользователя
        :return: httpx.Response
        """
        response = self.post(                                                # ▶ Запрос
            url=self.ENDPOINT,
            json=create_user_data.model_dump(by_alias=True))                 # Pydantic-model —> Dict (serialize)
        return response                                                      # httpx.Response


    # Pydantic-model
    @allure.step('Create user (Pydantic)')
    def create_user(self, create_user_data: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Pydantic-метод для создания нового пользователя

        :param create_user_data: Pydantic-model c данными для создания пользователя
        :return: Pydantic-model (CreateUserResponseSchema)
        """
        response = self.create_user_api(create_user_data)                             # ▶ Запрос через API-метод
        response_model = CreateUserResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (parsing-deserialize) (deserialize)
        return response_model                                                         # Pydantic-model (CreateUserResponseSchema)


#================================================= Client (✨Helper) ===================================================
@allure.step('Get Public Users Client')
def get_public_users_client() -> PublicUsersClient:
    """
    Функция получения экземпляра PrivateUsersClient с уже настроенным HTTP-клиентом (c Base URL)

    :return: Экземпляр PrivateUsersClient (с Base URL)
    """
    public_users_client = PublicUsersClient(client=get_httpx_public_client())
    return public_users_client

#-----------------------------------------------------------------------------------------------------------------------

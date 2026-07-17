"""
Users Client (Public)
(Для методов, НЕ требующих авторизации)
"""
import httpx
import allure
from tools.api_coverage import tracker
from tools.endpoints import Endpoint
from clients.api_client import APIClient
from clients.httpx_client_public import get_httpx_client_public
from schemas.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

#================================================ Users Client (Public) ================================================
class UsersClientPublic(APIClient):
    """
    Клиент для работы с /api/v1/users (Public)

    .
    """
    #------------------------------------------------- Create User  ----------------------------------------------------
    # API
    @allure.step('▶ Create User (API)')                               # Allure step Title
    @tracker.track_coverage_httpx(f'{Endpoint.USERS}')                # API Coverage tracker
    def create_user_api(self, create_user_data: CreateUserRequestSchema) -> httpx.Response:
        """
        API-метод создания нового пользователя

        :param create_user_data: Pydantic-model c данными для создания пользователя
        :return: httpx.Response
        """
        response = self.post(                                         # ▶ Запрос
            url=Endpoint.USERS,                                       # Endpoint (via Enum)
            json=create_user_data.model_dump(by_alias=True))          # Pydantic-model —> Dict (serialize)
        return response                                               # httpx.Response


    # Pydantic-model
    @allure.step('▶ Create User (Pydantic)')
    def create_user(self, create_user_data: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Pydantic-метод для создания нового пользователя

        :param create_user_data: Pydantic-model c данными для создания пользователя
        :return: Pydantic-model (CreateUserResponseSchema)
        """
        response = self.create_user_api(create_user_data)                             # ▶ Запрос через API-метод
        response_model = CreateUserResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)
        return response_model                                                         # Pydantic-model (CreateUserResponseSchema)



#================================================== Client (builder) ===================================================
@allure.step('◎ Get Users Client (Public)')
def get_users_client_public() -> UsersClientPublic:
    """
    Функция получения экземпляра UsersClientPublic() с настроенным httpx.Client (Public)

    :return: Настроенный экземпляр UsersClientPublic()
    """
    users_client_public = UsersClientPublic(client=get_httpx_client_public())
    return users_client_public                                        # UsersClientPublic()

#=======================================================================================================================

"""
Files Client
"""

import allure
import httpx
from pathlib import Path
from tools.api_coverage import tracker
from tools.endpoints import Endpoint
from clients.api_client import APIClient
from schemas.auth_schema import AuthDataSchema
from schemas.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from clients.httpx_client_private import get_httpx_client_private

#==================================================== Files Client =====================================================
class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files

    .
    """
    #---------------------------------------------------- Get File -----------------------------------------------------
    # API
    @allure.step('▶ Get File by ID (API)')                          # Allure step Title
    @tracker.track_coverage_httpx(f'{Endpoint.FILES}/{{file_id}}')  # API Coverage tracker (id - заэкранировано)
    def get_file_api(self, file_id: str) -> httpx.Response:
        """
        API-метод получения файла (Download) по File-ID

        :param file_id: File-ID
        :return: httpx.Response
        """
        response = self.get(url=f'{Endpoint.FILES}/{file_id}')      # ▶ Запрос
        return response                                             # httpx.Response


    # Pydantic-model
    @allure.step('▶ Get File by ID (Pydantic)')
    def get_file(self, file_id: str) -> GetFileResponseSchema:
        """
        Pydantic-метод получения файла (Download) по File-ID

        :param file_id: File-ID
        :return: httpx.Response
        """
        response = self.get_file_api(file_id)                                      # ▶ Запрос через API-метод
        response_model = GetFileResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)
        return response_model                                                      # Pydantic-model (GetFileResponseSchema)


    #--------------------------------------------------- Create File ---------------------------------------------------
    # API
    @allure.step('▶ Create File (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.FILES}')
    def create_file_api(self, create_file_data: CreateFileRequestSchema) -> httpx.Response:
        """
        API-метод создания файла (Upload).

        Файл передаётся байтами (не открытым файловым объектом),
        чтобы API Swagger Coverage tracker мог перечитать тело запроса после выполнения ("seek of closed file")

        :param create_file_data: Pydantic-model с данными о файле
        :return: httpx.Response
        """
        response = self.post(                                                       # ▶ Запрос:
            url=Endpoint.FILES,                                                     # URL запроса (endpoint через Enum)
            # data=create_file_data,  # целиком -> Сервер получит лишние поля: 'filename' и 'directory' (✔️ничего страшного)
            data={'filename': create_file_data.filename, 'directory': create_file_data.directory}, # Имя сохранения файла,  Директория сохранения
            files={'upload_file': Path(create_file_data.upload_path).read_bytes()}  # Содержимое файла (bytes)
        )
        return response                                                             # httpx.Response


    # Pydantic-model
    @allure.step('▶ Create File (Pydantic)')
    def create_file(self, create_file_data: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Pydantic-метод создания файла (Upload)

        :param create_file_data: Данные о создаваемом файле в формате Pydantic-model
        :return: Pydantic-model (CreateFileResponseSchema)
        """
        response = self.create_file_api(create_file_data)                             # ▶ Запрос через API-метод
        response_model = CreateFileResponseSchema.model_validate_json(response.text)  # httpx.Response —> Pydantic-model (deserialize)
        return response_model                                                         # Pydantic-model (CreateFileResponseSchema)


    #--------------------------------------------------- Delete File ---------------------------------------------------
    # API
    @allure.step('▶ Delete File by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.FILES}/{{file_id}}')   # API Coverage tracker (id - заэкранировано)
    def delete_file_api(self, file_id: str) -> httpx.Response:
        """
        API-метод удаления файла

        :param file_id: File-ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{Endpoint.FILES}/{file_id}')    # ▶ Запрос
        return response                                              # httpx.Response



#================================================== Client (builder) ===================================================
@allure.step('◎ Get Files Client')
def get_files_client(auth_data: AuthDataSchema) -> FilesClient:
    """
    Функция получения экземпляра FilesClient с настроенным HTTP-клиентом (с Авторизацией)

    :param auth_data: Pydantic-model c данными для аутентификации пользователя (Email, Password)
    :return: Экземпляр FilesClient (с Авторизацией)
    """
    files_client = FilesClient(client=get_httpx_client_private(auth_data))
    return files_client                                              # FilesClient()

#=======================================================================================================================

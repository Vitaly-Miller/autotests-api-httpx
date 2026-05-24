"""
Files Client
/files
(Клиент для работы с файлами)
"""
from urllib import response

import httpx
from clients.api_client import APIClient
from clients.auth.auth_schema import AuthUserSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_client_builder import get_private_http_client


#====================================================== Files Client ===================================================
class FilesClient(APIClient):
    ENDPOINT = '/files'
    #---------------------------------------------------- Get File -----------------------------------------------------
    # API
    def get_file_api(self, file_id: str) -> httpx.Response:
        """
        Метод для ПОЛУЧЕНИЯ (Download) файла по File ID

        :param file_id: File ID
        :return: httpx.Response
        """
        response = self.get(url=f'{self.ENDPOINT}/{file_id}')   # ▶ Запрос на получение файла по File ID
        return response                                         # httpx.Response

    #--------------------------------------------------- Create File ---------------------------------------------------
    # API
    def create_file_api(self, create_file_data: CreateFileRequestSchema) -> httpx.Response:
        """
        Метод для СОЗДАНИЯ (Upload) файла через with-контекстный менеджер (для закрытия после выполнения запроса)

        :param create_file_data: Данные о файле в формате Pydantic-model
        :return: httpx.Response
        """
        with open(create_file_data.upload_path, 'rb') as f:
            return self.post(             #  ▶ Запрос на создание файла:
                url=self.ENDPOINT,        # URL запроса
                # data=create_file_data,  # <- ⚠️проверить - create_file_data целиком -> Сервер получит лишние поля: 'filename' и 'directory' (✔️ничего страшного)
                data={'filename': create_file_data.filename, 'directory': create_file_data.directory}, # Имя сохранения файла,  Директория сохранения
                files={'upload_file': f}  # f - переменная прочитанного файла
            )

    # Pydantic-model
    def create_file(self, create_file_data: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Метод получения данных о созданном файле в формате Pydantic-model

        :param create_file_data: Данные о создаваемом файле в формате Pydantic-model
        :return: Ответ с данными о созданном файле в формате Pydantic-model
        """
        response = self.create_file_api(create_file_data)                   # ▶ Запрос на создание файла через API-метод
        return CreateFileResponseSchema.model_validate_json(response.text)  # Валидируем ответ (любой) —> Pydantic-model

    #--------------------------------------------------- Delete File ---------------------------------------------------
    # API
    def delete_file_api(self, file_id: str) -> httpx.Response:
        """
        Метод для удаления файла.

        :param file_id: File ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{self.ENDPOINT}/{file_id}')  # ▶ Запрос на удаление файла по File ID
        return response                                           # httpx.Response:



#================================================= Client (✨Helper) ===================================================
def get_files_client(auth_data: AuthUserSchema) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом (Base URL + Auth)

    :param auth_data: Данные для аутентификации пользователя (Email, Password)
    :return: Готовый к использованию FilesClient (Base URL + Auth)
    """
    return FilesClient(client=get_private_http_client(auth_data))

"""
Files Client
/files
(Клиент для работы с файлами)
"""
from httpx import Response
from clients.api_client import APIClient
from clients.auth.auth_schema import AuthUserSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import get_private_http_client

#===================================================== Client ==========================================================
class FilesClient(APIClient):
    ENDPOINT = '/files'
    #------------------------------------------------ Get File ---------------------------------------------------------
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод для ПОЛУЧЕНИЯ (Download) файла по File ID.

        :param file_id: File ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'/files/{file_id}')

    #----------------------------------------------- Create File -------------------------------------------------------
    def create_file_api(self, payload: CreateFileRequestSchema) -> Response:
        """
        Метод для СОЗДАНИЯ (Upload) файла через ✅with - контекстный менеджер (для закрытия после выполнения запроса)

        :param payload: Словарь с данными о файле.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        with open(payload.upload_path, 'rb') as f:
            return self.post(
                url=self.ENDPOINT,
                # data=payload,            # - ⚠️проверить - payload целиком -> Сервер получит лишние поля: 'filename' и 'directory' (✔️ничего страшного)
                data={'filename': payload.filename, 'directory': payload.directory},
                files={'upload_file': f}
            )

    def create_file(self, payload: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Метод получения валидированной Pydantic-model с данными о созданном файле.

        :param payload: Словарь с данными о файле.
        :return: Валидированная Pydantic-модель с данными об авторизации пользователя
        :return: JSON-объекта с данными о созданном файле
        """
        response = self.create_file_api(payload)
        return CreateFileResponseSchema.model_validate_json(response.text)  # ⚠ <- Валидируем ответ (любой) -> Model
        return response.json()                                              # ⚠ <- Может вызвать ошибку, если придет не JSON

    #------------------------------------------------ Delete File ------------------------------------------------------
    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод для удаления файла.

        :param file_id: File ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{self.ENDPOINT}/{file_id}')

    #-------------------------------------------------------------------------------------------------------------------

#=================================================== Client Builder =====================================================
def get_files_client(auth_data: AuthUserSchema) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :param auth_data: Данные для аутентификации пользователя (Email, Password)
    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(auth_data))

"""
Files Client
/files
(Клиент для работы с файлами)
"""
from httpx import Response
from clients.api_client import APIClient
from clients.authentication.authentication_schema import AuthenticationUserSchema
from clients.files.files_schema import CreateFileRequestSchema
from clients.users.private_http_builder import get_private_http_client

#=======================================================================================================================
#----------------------------------------------------- Client ----------------------------------------------------------
class FilesClient(APIClient):
    ENDPOINT = '/files'

    def get_file_api(self, file_id: str) -> Response:
        """
        Метод для ПОЛУЧЕНИЯ (download) файла по File ID.

        :param file_id: File ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'/files/{file_id}')

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        Метод для СОЗДАНИЯ (upload) файла через ✅with - контекстный менеджер (для закрытия после выполнения запроса)

        :param request: Словарь с данными файла (CreateFileRequestDict)
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        with open(request['upload_path'], 'rb') as f:
            return self.post(
                url=self.ENDPOINT,
                data=request,  # Request целиком -> Сервер получит лишнее поле file_path (✔️ничего страшного)
                files={'upload_file': f})

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод для удаления файла.

        :param file_id: File ID
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'{self.ENDPOINT}{file_id}')

#-----------------------------------------------------------------------------------------------------------------------
# Builder
def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))

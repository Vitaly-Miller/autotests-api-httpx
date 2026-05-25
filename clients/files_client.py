"""
Files Client
/files
(Клиент для работы с файлами)
"""
import httpx
from clients.api_client import APIClient
from schemas.auth import AuthUserSchema
from schemas.files import CreateFileRequestSchema, CreateFileResponseSchema
from clients.httpx_private_client import get_httpx_private_client


#====================================================== Files Client ===================================================
class FilesClient(APIClient):
    ENDPOINT = '/files'
    #---------------------------------------------------- Get File -----------------------------------------------------
    # API
    def get_file_api(self, file_id: str) -> httpx.Response:
        """
        API-метод получения файла (Download) по File ID

        :param file_id: File ID
        :return: httpx.Response
        """
        response = self.get(url=f'{self.ENDPOINT}/{file_id}')       # ▶ Запрос
        return response                                             # httpx.Response

    #--------------------------------------------------- Create File ---------------------------------------------------
    # API
    def create_file_api(self, create_file_data: CreateFileRequestSchema) -> httpx.Response:
        """
        API-метод создания файла (Upload) через with-контекстный менеджер (для закрытия после выполнения запроса)

        :param create_file_data: Pydantic-model с данными о файле
        :return: httpx.Response
        """
        with open(create_file_data.upload_path, 'rb') as f:
            response = self.post(                                   # ▶ Запрос:
                url=self.ENDPOINT,                                  # URL запроса
                # data=create_file_data,  # <- ⚠️проверить - create_file_data целиком -> Сервер получит лишние поля: 'filename' и 'directory' (✔️ничего страшного)
                data={'filename': create_file_data.filename, 'directory': create_file_data.directory}, # Имя сохранения файла,  Директория сохранения
                files={'upload_file': f}                            # f - переменная прочитанного файла
            )
            return response                                         # httpx.Response

    # Pydantic-model
    def create_file(self, create_file_data: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Pydantic-метод создания файла (Upload)

        :param create_file_data: Данные о создаваемом файле в формате Pydantic-model
        :return: Pydantic-model (CreateFileResponseSchema)
        """
        response = self.create_file_api(create_file_data)                    # ▶ Запрос через API-метод
        model = CreateFileResponseSchema.model_validate_json(response.text)  # Response —> Pydantic-model (deserialize)
        return model                                                         # Pydantic-model (CreateFileResponseSchema)

    #--------------------------------------------------- Delete File ---------------------------------------------------
    # API
    def delete_file_api(self, file_id: str) -> httpx.Response:
        """
        API-метод удаления файла

        :param file_id: File ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{self.ENDPOINT}/{file_id}')    # ▶ Запрос
        return response                                             # httpx.Response:



#================================================= Client (✨Helper) ===================================================
def get_files_client(auth_data: AuthUserSchema) -> FilesClient:
    """
    Функция получения экземпляра FilesClient с уже настроенным HTTP-клиентом (с Авторизацией)

    :param auth_data: Pydantic-model c данными для аутентификации пользователя (Email, Password)
    :return: Экземпляр FilesClient (с Авторизацией)
    """
    files_client = FilesClient(client=get_httpx_private_client(auth_data))
    return files_client

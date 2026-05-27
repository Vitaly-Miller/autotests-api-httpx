"""
Files Pydantic Schema
"""
from pathlib import Path
from pydantic import BaseModel, Field
from tools.data_generator import fake

#=======================================================================================================================
# Путь к файлу относительно текущего файла.
# .parents[1] - на 1 уровня вверх
file_path = Path(__file__).parents[1]/'testdata'/'files'/'test_image.png'
print(file_path)   # ▶︎ проверка корректности пути (optional)


"""================================================= ⬆︎REQUEST Schema ==============================================="""
#----------------------------------------------------- Create File -----------------------------------------------------
class CreateFileRequestSchema(BaseModel):
    """
    Схема для запроса на создание файла:

    filename:    Имя файла при сохранении на сервере
    directory:   Директория сохранения файла на сервере
    upload_path: Путь к файлу
    """
    filename: str = Field(default_factory=fake.png_file_name)  # Новое имя файла при сохранении на сервере
    directory: str = Field(default='Uploaded')                 # Директория сохранения файла на сервере
    upload_path: str = Field(default=file_path)                # Путь к файлу


"""================================================ ⬇︎RESPONSE Schema ==============================================="""
#----------------------------------------------------- Create File -----------------------------------------------------
class FileSchema(BaseModel):
    """
    Схема ключа "file":

    {
        id:        File ID
        filename:  Новое имя файла при сохранении на сервере
        directory: Директория сохранения файла на сервере
        url: str   URL-адрес файла
    }
    """
    id: str
    filename: str
    directory: str
    url: str

class CreateFileResponseSchema(BaseModel):
    """
    Схема ответа при создании файла

    .
    """
    file: FileSchema


"""===================================== File Full Schema (⬆︎Request + ⬇Response) ✨================================="""
class FileFullSchema(BaseModel):
    """
    Объединенная схема с данными о файле из Request + Response в формате Pydantic-model

    Request  -> Данные о файле из Request  (запрос)
    Response -> Данные о файле из Response (ответ)
    """
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema
    #------------------------------------- Методы для прямого доступа к данным -----------------------------------------
    # File ID
    @property
    def file_id(self):
        return self.response.file.id

    # File name (Новое имя файла при сохранении на сервере)
    @property
    def file_mame(self):
        return self.response.file.filename

    # Directory (Директория сохранения файла на сервере)
    @property
    def directory(self):
        return self.response.file.directory

#-----------------------------------------------------------------------------------------------------------------------

"""
Files Pydantic Schema
"""
from pydantic import BaseModel, Field
from tools.data_generator import fake

"""================================================= ⬆︎REQUEST Schema ==============================================="""
#----------------------------------------------------- Create File -----------------------------------------------------
class CreateFileRequestSchema(BaseModel):
    """
    Схема payload для запроса на создание файла:

    filename:    Имя файла при сохранении на сервере (Upload)
    directory:   Имя директории сохранения
    upload_path: Путь к файлу для загрузки
    """
    filename: str = Field(default_factory=fake.png_file_name)
    directory: str = Field(default='Uploaded')
    upload_path: str


"""================================================ ⬇︎RESPONSE Schema ==============================================="""
#----------------------------------------------------- Create File -----------------------------------------------------
class FileSchema(BaseModel):
    """
    Схема ключа "file":

    {
        id:        File ID
        filename:  Новое имя файла после сохранения на сервере
        directory: Имя директории сохранения
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
#-----------------------------------------------------------------------------------------------------------------------

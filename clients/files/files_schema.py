"""
Files Pydantic Schema
"""
from pydantic import BaseModel

#================================================== ⬆︎REQUEST Schema ===================================================
#----------------------------------------------------- Create File -----------------------------------------------------
class CreateFileRequestSchema(BaseModel):
    """
    Схема payload для запроса на создание файла:

    filename:    Имя файла
    directory:   Имя директории сохранения
    upload_path: Путь к файлу
    """
    filename: str
    directory: str
    upload_path: str


#================================================== ⬇︎RESPONSE Schema ==================================================
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

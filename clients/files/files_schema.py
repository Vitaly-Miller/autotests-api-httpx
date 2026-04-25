"""
Files Schema
"""
from pydantic import BaseModel

#=======================================================================================================================
#----------------------------------------------- REQUEST Pydantic Schemas ----------------------------------------------
class CreateFileRequestSchema(BaseModel):
    filename: str       # Имя файла
    directory: str      # Название Директории сохранения
    upload_path: str    # Путь к файлу



#---------------------------------------------- RESPONSE Pydantic Schemas ----------------------------------------------
class FileResponseSchema(BaseModel):
    """
    Схема словаря file при ответе на создание файла.
    """
    id: str
    filename: str
    directory: str
    url: str

class CreateFileResponseSchema(BaseModel):
    """
    Схема словаря ответа при создании файла.
    (create_file_api)
    """
    file: FileResponseSchema
#------------------------------------------

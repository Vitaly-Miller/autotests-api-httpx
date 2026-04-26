"""
Files Pydantic Schemas
"""
from pydantic import BaseModel

#=================================================== REQUEST schema ====================================================
#---------------------------------------------------- Create File ------------------------------------------------------
class CreateFileRequestSchema(BaseModel):
    filename: str       # Имя файла
    directory: str      # Название директории сохранения
    upload_path: str    # Путь к файлу


#=================================================== RESPONSE schema ===================================================
#---------------------------------------------------- Create File ------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------

"""
Files Schema
"""
from pydantic import BaseModel

#=======================================================================================================================
#-------------------------------------------------- Pydantic Schemas ---------------------------------------------------
class CreateFileRequestSchema(BaseModel):
    filename: str       # Имя файла
    directory: str      # Название Директории сохранения
    upload_path: str    # Путь к файлу

class File(BaseModel):
    id: str
    filename: str
    directory: str
    url: str

class CreateFileResponseSchema(BaseModel):
    file: File


#-----------------------------------------------------------------------------------------------------------------------

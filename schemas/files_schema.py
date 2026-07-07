"""
Files (Pydantic Schema)
"""
from config import settings
from pydantic import BaseModel, Field
from tools.data_generator import fake

#=======================================================================================================================
"""================================================= ⬆︎REQUEST Schema ==============================================="""
#----------------------------------------------------- Create File -----------------------------------------------------
class CreateFileRequestSchema(BaseModel):
    filename: str = Field(default_factory=fake.png_file_name)            # Новое имя файла при сохранении на сервере
    directory: str = Field(default='Uploaded')                           # Директория сохранения файла на сервере
    upload_path: str = Field(default=settings.test_data.image_png_file)  # Путь к файлу (from .env)


"""================================================ ⬇︎RESPONSE Schema ==============================================="""
#----------------------------------------------------- "file": {}  -----------------------------------------------------
class FileSchema(BaseModel):
    id: str           # File-ID
    filename: str     # Новое имя файла при сохранении на сервере
    directory: str    # Директория сохранения файла на сервере
    url: str          # URL-адрес файла на сервере

#----------------------------------------------------- Create File -----------------------------------------------------
class CreateFileResponseSchema(BaseModel):
    file: FileSchema

#----------------------------------------------------- Get File --------------------------------------------------------
class GetFileResponseSchema(BaseModel):
    file: FileSchema

#-----------------------------------------------------------------------------------------------------------------------
"""====================================== Full Schema (⬆︎Request + ⬇Response) ✨====================================="""
class CreateFileSchema(BaseModel):
    request: CreateFileRequestSchema    # ┐
    response: CreateFileResponseSchema  # ┘

    #--- Методы прямого доступа к данным ---
    # File-ID
    @property
    def file_id(self):
        return self.response.file.id

    # File name (Новое имя файла при сохранении на сервере)
    @property
    def file_mame(self):
        return self.request.filename

    # Directory (Директория сохранения файла на сервере)
    @property
    def directory(self):
        return self.request.directory

    # URL (Адрес файла на сервере)
    @property
    def url(self):
        return self.request.upload_path

#-----------------------------------------------------------------------------------------------------------------------

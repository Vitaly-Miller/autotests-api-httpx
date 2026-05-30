"""
Files Pydantic Schema
"""
from pathlib import Path
from pydantic import BaseModel, Field
from tools.data_generator import fake

#=======================================================================================================================
# Путь к файлу относительно текущего файла
file_path = Path(__file__).parents[1]/'testdata'/'files'/'test_image.png'   # .parents[1] - на 1 уровня вверх
print(file_path)                                                            # ▶︎ проверка корректности пути (optional)


"""================================================= ⬆︎REQUEST Schema ==============================================="""
#----------------------------------------------------- Create File -----------------------------------------------------
class CreateFileRequestSchema(BaseModel):
    filename: str = Field(default_factory=fake.png_file_name)  # Новое имя файла при сохранении на сервере
    directory: str = Field(default='Uploaded')                 # Директория сохранения файла на сервере
    upload_path: str = Field(default=file_path)                # Путь к файлу


"""================================================ ⬇︎RESPONSE Schema ==============================================="""
#----------------------------------------------------- Create File -----------------------------------------------------
class FileSchema(BaseModel):
    id: str           # File ID
    filename: str     # Новое имя файла при сохранении на сервере
    directory: str    # Директория сохранения файла на сервере
    url: str          # URL-адрес файла на сервере

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

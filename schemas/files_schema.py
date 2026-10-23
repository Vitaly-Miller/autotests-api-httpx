"""
Files (Pydantic Schema)
"""
from config import settings
from pydantic import BaseModel, Field
from tools.data_generator import fake

#================================================= ⬆︎REQUEST Schemas ===================================================
#----------------------------------------------------- Create File -----------------------------------------------------
class CreateFileRequestSchema(BaseModel):
    filename: str = Field(default_factory=fake.png_file_name)            # New file name when saved on the server
    directory: str = Field(default='Uploaded')                           # Directory where the file is saved on the server
    upload_path: str = Field(default=settings.test_data.image_png_file)  # File path (from .env)


#================================================= ⬇︎RESPONSE Schemas ==================================================
#----------------------------------------------------- "file": {}  -----------------------------------------------------
class FileSchema(BaseModel):
    id: str           # File-ID
    filename: str     # New file name when saved on the server
    directory: str    # Directory where the file is saved on the server
    url: str          # File URL on the server

#----------------------------------------------------- Create File -----------------------------------------------------
class CreateFileResponseSchema(BaseModel):
    file: FileSchema

#----------------------------------------------------- Get File --------------------------------------------------------
class GetFileResponseSchema(BaseModel):
    file: FileSchema


#======================================== Full Schema (⬆︎Request + ⬇Response) ✨=======================================
class CreateFileSchema(BaseModel):
    request: CreateFileRequestSchema    # ┐
    response: CreateFileResponseSchema  # ┘

    #--- Direct data access methods ---
    # File-ID
    @property
    def file_id(self):
        return self.response.file.id

    # File name (New file name when saved on the server)
    @property
    def file_mame(self):
        return self.request.filename

    # Directory (Directory where the file is saved on the server)
    @property
    def directory(self):
        return self.request.directory

    # URL (File address on the server)
    @property
    def url(self):
        return self.request.upload_path


#=======================================================================================================================

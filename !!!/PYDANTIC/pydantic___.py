"""
Pydantic ______
"""
import uuid

from faker import Faker
from pydantic import BaseModel, Field

#=======================================================================================================================
obj = {
  "course": {
    "id": "000",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "firstName": "string",
      "lastName": "string",
      "middleName": "string"
    }
  }
}

# Создаем Основную схему
class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: Faker().uuid4())             # 👈 Генерация уникального ID
    title: str = 'Playwright'
    max_score: int = Field(alias='maxScore', default=1000)
    min_score: int = Field(alias='minScore', default=100)
    description: str = 'POM'
    preview_file: FileSchema = Field(alias='previewFile')                  # из FileSchema
    estimated_time: str = Field(alias='estimatedTime', default='2 week')
    created_by_user: UserSchema = Field(alias='createdByUser')             # из UserSchema

# Вложенная схема для previewFile
class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: str

# Вложенная схема для createdByUser
class UserSchema(BaseModel):
    id: str
    email: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


#-------------------------------------------------------- Model --------------------------------------------------------
# Инициализация модели (классическая)
course_model = CourseSchema(
    id='111',
    title='Playwright',
    maxScore=100,
    minScore=10,
    description='POM',
    previewFile=FileSchema(
        id='File_id',
        filename='file.txt',
        directory='files',
        url='https://example.com/file.txt'
    ),
    estimatedTime='1 week',
    createdByUser=UserSchema(
        id='User_id',
        email='user@example.com',
        lastName='Connor',
        firstName='John',
        middleName='Middle'
    )
)

# Dict
course_dict = {
    'id': '222',
    'title': 'Playwright',
    'maxScore': 100,
    'minScore': 10,
    'description': 'POM',
    'previewFile': {
        'id': 'File_id',
        'filename': 'file.txt',
        'directory': 'files',
        'url': 'https://example.com/file.txt'
    },
    'estimatedTime': '1 week',
    'createdByUser': {
        'id': 'User_id',
        'email': 'user@example.com',
        'firstName': 'John',
        'lastName': 'Connor',
        'middleName': 'Middle'
    }
}

# JSON
course_json = """
{
    "id": "333",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "POM",
    "previewFile": {
        "id": "File_id",
        "filename": "file.txt",
        "directory": "files",
        "url": "https://example.com/file.txt"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "User_id",
        "email": "user@example.com",
        "firstName": "John",
        "lastName": "Connor",
        "middleName": "Middle"
    }
}
"""


#-----------------------------------------------------------------------------------------------------------------------
# Output
print('---------------------')
print(f'Model | {course_model}') # id='111' title='Playwright' max_score=100 min_score=10 description='POM' preview_file=FileSchema(id='File_id', filename='file.txt', directory='files', url='https://example.com/file.txt') estimated_time='1 week' created_by_user=UserSchema(id='User_id', email='user@example.com', first_name='John', last_name='Connor', middle_name='Middle')
print(f'Dict  | {course_dict}')  # {'id': '222', 'title': 'Playwright', 'maxScore': 100, 'minScore': 10, 'description': 'POM', 'previewFile': {'id': 'File_id', 'filename': 'file.txt', 'directory': 'files', 'url': 'https://example.com/file.txt'}, 'estimatedTime': '1 week', 'createdByUser': {'id': 'User_id', 'email': 'user@example.com', 'firstName': 'John', 'lastName': 'Connor', 'middleName': 'Middle'}}
print(f'JSON  | {course_json}')  # {"id": "333", "title": "Playwright", "maxScore": 100, "minScore": 10, "description": "POM", "previewFile": {"id": "File_id", "filename": "file.txt", "directory": "files", "url": "https://example.com/file.txt"}, "estimatedTime": "1 week", "createdByUser": {"id": "User_id", "email": "user@example.com", "firstName": "John", "lastName": "Connor", "middleName": "Middle"}}
print('---------------------')

# Serializing
print('Serializing:')
course_model_json = course_model.model_dump()                         # Model -> {dict} (🐍snake_case)
print(f'Model -> Dict         | {course_model_json}')

course_model_json = course_model.model_dump(by_alias=True)            # Model -> {dict} (🐫camelCase)
print(f'Model -> Dict (alias) | {course_model_json}')

course_model_json = course_model.model_dump_json()                    # Model -> JSON   (🐍snake_case)
print(f'Model -> JSON         | {course_model_json}')

course_model_json_alias = course_model.model_dump_json(by_alias=True) # Model -> JSON   (🐫camelCase)
print(f'Model -> JSON (alias) | {course_model_json_alias}')

"""
API Client Create Exercise
"""
from clients.auth.auth_schema import AuthUserSchema
from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.data_generator import fake

#=======================================================================================================================
#---------------------------------------------------- 1. Create User ---------------------------------------------------
# Инициализация Pydantic Model
create_user_payload = CreateUserRequestSchema()           # Модель с данными о новом пользователе

# Инициализация клиента (public)
users_client = get_public_users_client()

# 🟨POST запрос на создание пользователя методом create_user
create_user_response = users_client.create_user(payload=create_user_payload)


#--------------------------------------------------- 2. Create File  ---------------------------------------------------
# Инициализация Pydantic Model
auth_data = AuthUserSchema(                             # Модель с данными для аутентификации
    email=create_user_payload.email,                    # Берем email из create_user_payload модели
    password=create_user_payload.password               # Берем password из create_user_payload модели
)

# Инициализация клиента (private)
files_client = get_files_client(auth_data=auth_data)

# Инициализация Pydantic Model
create_file_payload = CreateFileRequestSchema(          # Модель с данными о файле
    upload_path="testdata/my_files/my_image.png"
)
# 🟨POST запрос на создание файла методом create_file
create_file_response = files_client.create_file(payload=create_file_payload) # Сохраняем ответ


#-------------------------------------------------- 3. Create Course  --------------------------------------------------
# Инициализация Pydantic Model
create_course_payload = CreateCourseRequestSchema(      # Модель с данными о курсе
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)

# Инициализация клиента (private)
courses_client = get_courses_client(auth_data=auth_data)

# 🟨POST запрос на создание куса методом create_course
create_course_response = courses_client.create_course(payload=create_course_payload)

#-------------------------------------------------- 4. Create Exercise  ------------------------------------------------
create_exercise_payload = CreateExerciseRequestSchema(  # Модель c данными о задании
    title='Exercise 1',
    courseId=create_course_response.course.id,
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description='Find a bug',
    estimatedTime='5 min',
)

# Инициализация клиента (private)
exercise_client = get_exercise_client(auth_data=auth_data)

# 🟨POST запрос на создание задания методом create_exercise
create_exercise_response = exercise_client.create_exercise(payload=create_exercise_payload)


#------------------------------------------------------ Output ---------------------------------------------------------
print(f'    User ID: {create_user_response.user.id}')
print(f'    File ID: {create_file_response.file.id}')
print(f'  Course ID: {create_course_response.course.id}')
print(f'Exercise ID: {create_exercise_response.exercise.id}')
#-----------------------------------------------------------------------------------------------------------------------

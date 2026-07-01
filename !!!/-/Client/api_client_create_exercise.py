"""
API Client Create Exercise
"""
from schemas.auth_schema import AuthDataSchema
from clients.courses_client import get_courses_client
from schemas.courses_schema import CreateCourseRequestSchema
from clients.exercises_client import get_exercises_client
from schemas.exercises_schema import CreateExerciseRequestSchema
from clients.files_client import get_files_client
from schemas.files_schema import CreateFileRequestSchema
from clients.public_users_client import get_public_users_client
from schemas.users_schema import CreateUserRequestSchema

#===================================================== [PRECONDITION] ==================================================
#---------------------------------------------------- 1. Create User ---------------------------------------------------
# Инициализация Pydantic Model
create_user_data = CreateUserRequestSchema()    # Инициализация данных через схему c fake данными

# Инициализация PublicUsersClient (экземпляр класса через Helper)
public_users_client = get_public_users_client()

# 🟨POST запрос на создание пользователя методом create_user (на выходе -> Pydantic-Model)
create_user_response = public_users_client.create_user(create_user_data=create_user_data)

# Авторизационные данные
auth_data = AuthDataSchema(                  # Инициализация модели / Валидация данных через схему
    email=create_user_data.email,            # Вытаскиваем email из create_user_data модели
    password=create_user_data.password       # Вытаскиваем password из create_user_data модели
)
#--------------------------------------------------- 2. Create File  ---------------------------------------------------
# Инициализация FilesClient (экземпляр класса через Helper)
files_client = get_files_client(auth_data=auth_data)

# Инициализация Pydantic-model с данными о файле
create_file_data = CreateFileRequestSchema(
    upload_path="../../../testdata/files/test_image.png"
)
# 🟨POST запрос на создание файла методом create_file
create_file_response = files_client.create_file(create_file_data=create_file_data)


#-------------------------------------------------- 3. Create Course  --------------------------------------------------
# Инициализация Pydantic-model с данными о курсе
create_course_data = CreateCourseRequestSchema(      # Модель с данными о курсе
    previewFileId=create_file_response.file.id,         # ⚠ Обращение через .атрибут - Для валидированной Pydantic-Model
    createdByUserId=create_user_response.user.id        # ⚠ Обращение через .атрибут - Для валидированной Pydantic-Model
)

# Инициализация CoursesClient (экземпляр класса через Helper)
courses_client = get_courses_client(auth_data=auth_data)

# 🟨POST запрос на создание куса методом create_course
create_course_response = courses_client.create_course(create_course_data=create_course_data)

#==================================================== Create Exercise ==================================================
# Инициализация Pydantic-model с данными о задании
create_exercise_data = CreateExerciseRequestSchema(
    courseId=create_course_response.course.id
)

# Инициализация ExercisesClient (экземпляр класса через Helper)
exercise_client = get_exercises_client(auth_data=auth_data)

# 🟨POST запрос на создание задания методом create_exercise
create_exercise_response = exercise_client.create_exercise(create_exercise_data=create_exercise_data)


#------------------------------------------------------ Output ---------------------------------------------------------
print(f'    User-ID: {create_user_response.user.id}')
print(f'    File-ID: {create_file_response.file.id}')
print(f'  Course ID: {create_course_response.course.id}')
print(f'Exercise ID: {create_exercise_response.exercise.id}')

#-----------------------------------------------------------------------------------------------------------------------

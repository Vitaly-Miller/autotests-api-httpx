"""
Config (Pydantic-settings)
"""
from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


#================================================== Settings Classes ===================================================
#----------------------------------------------------- Sub-Classes -----------------------------------------------------
class HTTPXClientConfig(BaseModel):
    base_url: str | HttpUrl
    timeout: float | int | None = None

    #╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    # Использовать, если base_url: HttpUrl
    @property
    def base_url_str(self) -> str:
        """
        HttpUrl —> 'str'

        Использовать, если base_url: HttpUrl (Pydantic-аннотация)

        :return: Base URL (string)
        """
        return str(self.base_url)
    #╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘

class TestDataConfig(BaseModel):
    image_png_file: FilePath


#----------------------------------------------------- MAIN Class ------------------------------------------------------
class Settings(BaseSettings):
    model_config = SettingsConfigDict(        # CONFIG файла с переменными окружения (.env)
        env_file='.env',                      # - Название файла с переменными окружения (.env)
        env_file_encoding='utf-8',            # - Кодировка файла с переменными окружения (.env)
        env_nested_delimiter='.'              # - Разделитель вложенных моделей в .env (ex. HTTPX_CLIENT.BASE_URL='...')
    )
    # Вложенные Pydantic-models:
    httpx_client: HTTPXClientConfig
    test_data: TestDataConfig



#========================================== Helper ✨(ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ) ===========================================
settings = Settings()                         # Инициализация класса-Pydantic-model (Settings)

#=======================================================================================================================

"""
Config (via Pydantic-settings)
"""
from pathlib import Path
from pydantic import BaseModel, HttpUrl, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict

#================================================== Settings Classes ===================================================
#----------------------------------------------------- Sub-Classes -----------------------------------------------------
class HTTPXClientConfig(BaseModel):
    base_url: str | HttpUrl
    timeout: float | int | None = None

    #╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    # Use if base_url: HttpUrl
    @property
    def base_url_str(self) -> str:
        """
        HttpUrl —> 'str'

        Use when base_url: HttpUrl (Pydantic annotation)

        :return: Base URL (string)
        """
        return str(self.base_url)
    #╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘

class TestDataConfig(BaseModel):
    image_png_file: FilePath


#---------------------------------------------- MAIN Class + .env-config -----------------------------------------------
class Settings(BaseSettings):
    model_config = SettingsConfigDict(        # CONFIG of the environment variables file (.env)
        extra='allow',                        # Allow extra variables (e.g. for CI) (optional)
        env_file='.env',                      # - Environment variables file name (.env)
        env_file_encoding='utf-8',            # - Environment variables file encoding (.env)
        env_nested_delimiter='.'              # - Nested models delimiter in .env (ex. HTTPX_CLIENT.BASE_URL='...')
    )
    # Nested Pydantic models:
    httpx_client: HTTPXClientConfig
    test_data: TestDataConfig
    allure_results_dir: Path = Path('allure-results')
    # allure_results_dir: DirectoryPath


    # #-------------- Creates the folder if it does not exist --------------
    # @classmethod
    # def initialize(cls) -> "Settings":
    #     allure_results_dir = DirectoryPath('allure-results')   # Folder name
    #     allure_results_dir.mkdir(exist_ok=True)                # Creates the folder if it does not exist
    #
    #     return Settings(allure_results_dir=allure_results_dir)


#--------------------------------------------------- Helper ✨ ---------------------------------------------------------
#settings = Settings.initialize()      # Initialize Pydantic model class (Settings) via .initialize
settings = Settings()                  # Initialize Pydantic model class (Settings)


#=======================================================================================================================

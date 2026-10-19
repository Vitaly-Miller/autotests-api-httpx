"""
Files Client
"""

import allure
import httpx
from pathlib import Path
from tools.api_coverage import tracker
from tools.endpoints import Endpoint
from clients.api_client import APIClient
from schemas.auth_schema import AuthDataSchema
from schemas.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from clients.httpx_client_private import get_httpx_client_private


#==================================================== Files Client =====================================================
class FilesClient(APIClient):
    """
    Client for working with /api/v1/files

    .
    """
    #---------------------------------------------------- Get File -----------------------------------------------------
    # API
    @allure.step('▶ Get File by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.FILES}/{{file_id}}')
    def get_file_api(self, file_id: str) -> httpx.Response:
        """
        API method for getting (downloading) a file by File-ID

        :param file_id: File-ID
        :return: httpx.Response
        """
        response = self.get(url=f'{Endpoint.FILES}/{file_id}')
        return response


    # Pydantic-model
    @allure.step('▶ Get File by ID (Pydantic)')
    def get_file(self, file_id: str) -> GetFileResponseSchema:
        """
        Pydantic method for getting (downloading) a file by File-ID

        :param file_id: File-ID
        :return: Pydantic-model (GetFileResponseSchema)
        """
        response = self.get_file_api(file_id)
        response_model = GetFileResponseSchema.model_validate_json(response.text)
        return response_model


    #--------------------------------------------------- Create File ---------------------------------------------------
    # API
    @allure.step('▶ Create File (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.FILES}')
    def create_file_api(self, create_file_data: CreateFileRequestSchema) -> httpx.Response:
        """
        API method for creating (uploading) a file.

        The file is sent as bytes (not as an open file object)
        so that the API Swagger Coverage tracker can re-read the request body afterwards ("seek of closed file")

        :param create_file_data: Pydantic model with file data
        :return: httpx.Response
        """
        response = self.post(
            url=Endpoint.FILES,
            data={'filename': create_file_data.filename, 'directory': create_file_data.directory},
            files={'upload_file': Path(create_file_data.upload_path).read_bytes()}
        )
        return response


    # Pydantic-model
    @allure.step('▶ Create File (Pydantic)')
    def create_file(self, create_file_data: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Pydantic method for creating (uploading) a file

        :param create_file_data: Data of the file to create as a Pydantic model
        :return: Pydantic-model (CreateFileResponseSchema)
        """
        response = self.create_file_api(create_file_data)
        response_model = CreateFileResponseSchema.model_validate_json(response.text)
        return response_model


    #--------------------------------------------------- Delete File ---------------------------------------------------
    # API
    @allure.step('▶ Delete File by ID (API)')
    @tracker.track_coverage_httpx(f'{Endpoint.FILES}/{{file_id}}')
    def delete_file_api(self, file_id: str) -> httpx.Response:
        """
        API method for deleting a file by File-ID

        :param file_id: File-ID
        :return: httpx.Response
        """
        response = self.delete(url=f'{Endpoint.FILES}/{file_id}')
        return response



#================================================== Client (builder) ===================================================
@allure.step('◎ Get Files Client')
def get_files_client(auth_data: AuthDataSchema) -> FilesClient:
    """
    Returns a FilesClient instance with a preconfigured HTTP client (with authorization)

    :param auth_data: Pydantic model with user authentication data (email, password)
    :return: FilesClient instance (with authorization)
    """
    files_client = FilesClient(client=get_httpx_client_private(auth_data))
    return files_client


#=======================================================================================================================

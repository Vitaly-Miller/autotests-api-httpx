"""
сonftest.py
Хранение фикстур
"""
import pytest
from clients.auth.auth_client import get_auth_client, AuthClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient

#=======================================================================================================================
# Authentication client
@pytest.fixture                                     # Default scope='function'
def auth_client() -> AuthClient:
    return get_auth_client()


# Инициализация client (public)
@pytest.fixture                                     # Default scope='function'
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

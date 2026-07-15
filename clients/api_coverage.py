"""
API Coverage
"""
from swagger_coverage_tool import SwaggerCoverageTracker

#=======================================================================================================================

tracker = SwaggerCoverageTracker(service='api-service')    # Инициализация трекера покрытия + key из .env





import httpx

# Оборачиваем функцию вызова GET-запроса в декоратор трекера
@tracker.track_coverage_httpx("/api/v1/users/{user_id}")
def get_user(user_id: str):
    return httpx.get(f"http://localhost:8000/api/v1/users/{user_id}")

# Аналогично оборачиваем POST-запрос
@tracker.track_coverage_httpx("/api/v1/users")
def create_user():
    return httpx.post("http://localhost:8000/api/v1/users")

# Вызываем функции, чтобы они попали в отчет покрытия
get_user("123")
create_user()

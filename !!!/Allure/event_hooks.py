"""
Event hooks (хуки событий)
— параметр httpx.Client, позволяющий выполнять дополнительные действия перед Request запроса или после Response
"""
import httpx

#=======================================================================================================================
# Функция для Event Hooks
def print_request(request: httpx.Request):                       # Функция для Event Hooks принимает Request
    print(f'Выполняю {request.method}-request')                  # Action

# Event Hooks - прописываем в httpx.Client
client = httpx.Client(event_hooks={'request': [print_request]})   # до Request выполнить функцию print_request


#-----------------------------------------------------------------------------------------------------------------------
# HTTP-запросы
client.get('http://localhost:8000/api/v1/users')      # Выполняю GET-request
client.post('http://localhost:8000/api/v1/users')     # Выполняю POST-request
client.patch('http://localhost:8000/api/v1/users')    # Выполняю PATCH-request
client.delete('http://localhost:8000/api/v1/users')   # Выполняю DELETE-request

#=======================================================================================================================

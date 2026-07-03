"""
Event hooks (хуки событий) в httpx
— выполнять дополнительные действия перед Request запроса или после Response
"""
import httpx

#=======================================================================================================================
# Функция для Event Hooks
def print_request(request: httpx.Request):
    print(f'{request.method}-request to {request.url}')

# Event Hooks
client = httpx.Client(event_hooks={'request': [print_request]})   # до Request выполнить функцию print_request


#-----------------------------------------------------------------------------------------------------------------------
# HTTP-запросы
client.get('http://localhost:8000/api/v1/users')      # GET-request to http://localhost:8000/api/v1/users
client.post('http://localhost:8000/api/v1/users')     # POST-request to http://localhost:8000/api/v1/users
client.patch('http://localhost:8000/api/v1/users')    # PATCH-request to http://localhost:8000/api/v1/users
client.delete('http://localhost:8000/api/v1/users')   # DELETE-request to http://localhost:8000/api/v1/users

#=======================================================================================================================

"""
cURL command generator
"""
import httpx

#=======================================================================================================================
# cURL
def make_curl_from_request(request: httpx.Request) -> str:
    """
    Генерирует команду cURL из httpx.Request.

    :param request: HTTP-запрос, из которого будет сформирована команда cURL.
    :return: Строка с командой cURL, содержащая метод запроса, URL, заголовки и тело (если есть).
    """
    # Создаем список с основной командой cURL, включая Метод и URL
    result: list[str] = [f'curl -X "{request.method}"', f'"{request.url}"']  # Генерируем сроковый список

    # Добавляем заголовки в формате -H "Header: Value"
    for header, value in request.headers.items():         # Итерация по заголовкам и значениям headers
        result.append(f'-H "{header}: {value}"')          # Добавление заголовков и значений в <result>

    # Добавляем body, если оно есть (например, для POST, PUT, UPDATE)
    try:
        if request.content:                                # Если есть request.content (body), то ...  ┐ ИЛИ ОДНОЙ СТРОКОЙ —> if body := request.content:
            body = request.content                         # ... сохраняем в <body>                    ┘
            result.append(f'-d "{body.decode('utf-8')}"')  # Добавление body в <result> c переводом байтов в —> строку
    except httpx.RequestNotRead:                           # Если запрос не прочитан, в случае передачи stream, ...
        pass                                               # ... проигнорировать

    # Объединение списка строк result в одну строку (через склеивание .join())
    return " \\\n  ".join(result)                          # <пробел>, разделитель-<\> (экранированный), перенос сроки-<\n>, <пробел>, <пробел>

#=======================================================================================================================

# Запуск проекта:
`docker compose up`

# Тестовые данные
`uv run python3 uv run python3 generate_test_data.py `
или воспользоваться приложенной коллекцией Postman
`REST.postman_collection.json`

# Авторизация
Для моковой авторизации просто добавьте заголовок `{user_id: "{id}"}` чтобы симулировать работу разных пользователей


# Подключение к вэбсокету
URL: `ws://localhost:8000/ws/`
пример сообщения: 
`{
    "method": "send_message",
    "payload": {
        "text": "Всем привет",
        "chat_id": 2
    }
}
`

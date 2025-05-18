# Запуск проекта:
`docker compose up`

# Тестовые данные
`uv run python3 uv run python3 generate_test_data.py `
или воспользоваться приложенной коллекцией Postman
`REST.postman_collection.json`

# Авторизация
Для моковой авторизации просто добавьте заголовок `{user_id: "{id}"}` чтобы симулировать работу разных пользователей

`curl --location 'http://localhost:8000/rest/v1/chats/2/' --header 'user_id: 1'`

# Подключение к вэбсокету
URL: `ws://localhost:8000/ws/`
пример сообщений: 

`{
    "method": "send_message",
    "payload": {
        "text": "Всем привет",
        "chat_id": 2
    }
}
`

`{
    "method": "read_message",
    "payload": {
        "chat_id": 2,
        "message_id": 16
    }
}`

import requests
from urllib.parse import urljoin
import json
import random
from string import ascii_letters

BASE_URL = "http://localhost:8000/rest/v1/"
HEADERS = {"user_id": "1"}


def create_random_user():

    r = requests.post(urljoin(BASE_URL, "users/"), json.dumps({
        "name": f"user {random.randint(1, 100)}",
        "email": f"{''.join(random.sample(ascii_letters, 10))}@mail.ru",
        "password": ''.join(random.sample(ascii_letters, 10))
    }), headers=HEADERS)
    print(r)


def create_chat():
    participants = random.sample([1,2,3,4,5], random.randint(2,4))

    requests.post(urljoin(BASE_URL, "chats/"), json.dumps({
        "name": f"chat {random.randint(1, 100)}",
        "participants": participants,
        "type": "group" if len(participants) > 2 else "private"
    }), headers=HEADERS)




if __name__ == '__main__':
    for _ in range(5):
        create_random_user()

    for _ in range(3):
        create_chat()


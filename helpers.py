import allure
import requests
from faker import Faker


@allure.step('Создаем пользователя')
def create_user():
    fake = Faker()
    user = {
        'email': fake.email(),
        'password': fake.password(),
        'name': fake.user_name()
    }
    payload = {
        'email': user['email'],
        'password': user['password'],
        'name': user['name']
    }
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
    user['accessToken'] = response.json()['accessToken']
    return user


@allure.step('Удаляем пользователя')
def delete_user(user):
    headers = {
        'authorization': user['accessToken']
    }
    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers)




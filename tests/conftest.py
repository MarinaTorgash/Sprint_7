import pytest
import generators
import requests
from urls import Url

@pytest.fixture()
def create_and_login_courier():
    login = generators.generate_login()
    password = generators.generate_password()
    name = generators.generate_name()

    courier_data = {'login': login, 'password': password, 'firstName': name}
    login_data = {'login': login, 'password': password}

    # Создаём курьера
    create_response = requests.post(Url.CREATE_COURIER, json=courier_data)
    assert create_response.status_code == 201, "Не удалось создать курьера в фикстуре"

    # Логинимся
    login_response = requests.post(Url.LOGIN_COURIER, json=login_data)
    assert login_response.status_code == 200, "Не удалось залогиниться в фикстуре"

    courier_id = login_response.json().get("id")
    assert courier_id is not None, "ID курьера не получен"

    yield {
        'courier_data': courier_data,
        'login_data': login_data,
        'courier_id': courier_id
    }
    requests.delete(f'{Url.DELETE_COURIER}{courier_id}')

@pytest.fixture()
def generate_courier_data():
    login = generators.generate_login()
    password = generators.generate_password()
    name = generators.generate_name()
    create_courier_body = {'login': login, 'password': password, 'firstName': name}
    login_courier_body = {'login': login, 'password': password}
    yield create_courier_body
    login_courier = requests.post(Url.LOGIN_COURIER, json=login_courier_body)
    requests.delete(f'{Url.DELETE_COURIER}{login_courier.json()["id"]}')
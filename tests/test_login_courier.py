import pytest
from urls import Url
import allure
import requests
from data import DataForuthorization, LoginCourier
import generators


class TestLoginCourier:

    @allure.title('Успешная авторизация курьера. Handle: /api/v1/courier/login')
    def test_login_courier_successful(self, create_and_login_courier):
        login_data = create_and_login_courier['login_data']

        with allure.step('Отправка запроса на авторизацию курьера'):
            response = requests.post(Url.LOGIN_COURIER, json=login_data)

        with allure.step('Проверка успешной авторизации и получения ID курьера'):
            courier_id = response.json().get("id")
            assert response.status_code == 200 and courier_id != ''

    @allure.title('Попытка авторизации курьера без регистрации. Handle: /api/v1/courier/login')
    def test_login_courier_without_registration_return_error(self):
        with allure.step('Генерация случайных логина и пароля (несуществующий курьер)'):
            login_data = {
                'login': generators.generate_login(),
                'password': generators.generate_password()
            }

        with allure.step('Отправка запроса на авторизацию несуществующего курьера'):
            response = requests.post(Url.LOGIN_COURIER, json=login_data)

        with allure.step('Проверка ошибки 404 и сообщения об отсутствии учётной записи'):
            assert response.status_code == 404 and response.json() == LoginCourier.COURIER_LOGIN_NON_REGISTRATION

    @allure.title('Попытка авторизации курьера при отсутствии логина или пароля. Handle: /api/v1/courier/login')
    @pytest.mark.parametrize('data', DataForuthorization.data_log)
    def test_login_courier_without_login_or_password_return_error(self, data):
        with allure.step('Отправка запроса на авторизацию с неполными данными: {}'.format(data)):
            response = requests.post(Url.LOGIN_COURIER, json=data)

        with allure.step('Проверка ошибки 400 и сообщения о нехватке данных'):
            assert response.status_code == 400 and response.json() == LoginCourier.COURIER_LOGIN_WITHOUT_LOGIN_OR_PASSWORD



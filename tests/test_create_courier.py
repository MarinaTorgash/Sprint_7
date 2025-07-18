import pytest
from urls import Url
import allure
import requests
from data import CreationCourier, DataForRegistration


class TestCreateNewCourier:

    @allure.title('Успешная регистрация нового курьера. Handle: /api/v1/courier')
    def test_create_courier_success(self, generate_courier_data):
        with allure.step('Отправка запроса на создание курьера'):
            response = requests.post(Url.CREATE_COURIER, json=generate_courier_data)

        with allure.step('Проверка, что курьер успешно создан'):
            assert response.status_code == 201 and response.json() == CreationCourier.COURIER_CREATION_SUCCESS

    @allure.title('Попытка зарегистрировать существующего курьера. Handle: /api/v1/courier')
    def test_create_courier_duplicate_courier_return_error(self, create_and_login_courier):
        courier_data = create_and_login_courier['courier_data']

        with allure.step('Отправка запроса на повторную регистрацию уже существующего курьера'):
            response = requests.post(Url.CREATE_COURIER, json=courier_data)

        with allure.step('Проверка, что API вернул ошибку 409 и соответствующее сообщение'):
            assert response.status_code == 409 and response.json() == CreationCourier.COURIER_NAME_ALREADY_EXIST

    @allure.title('Попытка зарегистрировать курьера при отсутствии логина или пароля. Handle: /api/v1/courier')
    @pytest.mark.parametrize('data', DataForRegistration.data_reg)
    def test_create_courier_without_login_or_password_return_error(self, data):
        with allure.step('Отправка запроса на регистрацию с неполными данными'):
            response = requests.post(Url.CREATE_COURIER, json=data)

        with allure.step('Проверка, что API вернул ошибку 400 и сообщение о нехватке данных'):
            assert response.status_code == 400 and response.json() == CreationCourier.COURIER_CREATION_WITHOUT_DATA


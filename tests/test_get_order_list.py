from urls import Url
import allure
import requests
from data import Flags


class TestOrderList:

    @allure.title('Успешное получение списка заказов. Handle: /api/v1/orders')
    def test_get_order_list_successful(self):
        with allure.step('Отправка запроса на получение списка заказов'):
            response = requests.get(Url.GET_LIST_ORDERS)

        with allure.step('Проверка, что список заказов успешно получен'):
            assert response.status_code == 200
            assert Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()


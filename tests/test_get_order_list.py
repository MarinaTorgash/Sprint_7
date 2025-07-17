from urls import Url
import allure
import requests
from data import Flags


class TestOrderList:

    @allure.title('Успешное получение списка заказов. Handle: /api/v1/orders/track')
    def test_get_order_list_successful(self):
        response = requests.get(Url.GET_LIST_ORDERS)
        assert response.status_code == 200 and Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()


from urls import Url
import allure
import requests
from data import OrderData, Flags
import pytest


class TestCreateOrder:

    @allure.title('Успешное создание списка заказов. Handle: /api/v1/orders')
    @pytest.mark.parametrize('scooter_color', OrderData.scooter_color)
    def test_create_order_with_color_successful(self, scooter_color):
        order_data = OrderData.order_data
        order_data['color'] = scooter_color
        order = requests.post(Url.CREATE_ORDER, json=order_data)
        assert order.status_code == 201 and Flags.SUCCESSFUL_CREATION_ORDER in order.json()
        requests.put(f'{Url.ORDER_CANCEL}{order.json()["track"]}')


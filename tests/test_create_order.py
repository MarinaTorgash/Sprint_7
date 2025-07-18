import allure
from data import OrderData, Flags
import pytest


class TestCreateOrder:

    @allure.title('Успешное создание списка заказов. Handle: /api/v1/orders')
    @pytest.mark.parametrize('create_and_cleanup_order', OrderData.scooter_color, indirect=True)
    def test_create_order_with_color_successful(self, create_and_cleanup_order):
        response = create_and_cleanup_order

        with allure.step('Проверка успешного создания заказа'):
            assert response.status_code == 201 and 'track' in response.json()

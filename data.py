import generators

class OrderData:
    order_data = {
            'name': 'Иван',
            'last_name': 'Иванов',
            'address': 'ул. Пушкина, д. 10',
            'metro': 'Сокольники',
            'phone': '+79991234567',
            'date': '01.01.2025',
            'rental_period': 'трое суток',
            'color': 'black',
            'comment': 'Позвонить за час'
    }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']] #для параметризации

class DataForRegistration:
    data_reg = [
        {'login': '', 'password': generators.generate_password(), 'name': generators.generate_name()},
        {'login': generators.generate_login(), 'password': '', 'name': generators.generate_name()}
    ]
class DataForuthorization:
    data_log = [
        {'login': '', 'password': generators.generate_password()},
        {'login': generators.generate_login(), 'password': ''}
    ]

class CreationCourier:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_CREATION_WITHOUT_DATA = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    COURIER_NAME_ALREADY_EXIST = {'code': 409, 'message': 'Этот логин уже используется'}

class LoginCourier:
    COURIER_LOGIN_WITHOUT_LOGIN_OR_PASSWORD = {'code': 400, 'message': 'Недостаточно данных для входа'}
    COURIER_LOGIN_NON_REGISTRATION = {'code': 404, 'message': 'Учетная запись не найдена'}

class DeleteCourier:
    COURIER_DELETE_SUCCESS = {'ok': True}
    COURIER_DELETE_WITHOUT_ID = {'code': 400, 'message': 'Недостаточно данных для удаления курьера'}
    COURIER_DELETE_NON_EXISTENT_ID = {'code': 409, 'message': 'Курьера с таким id нет'}

class Flags:
    SUCCESSFUL_CREATION_ORDER = 'track' #флаг успешного создания заказа
    SUCCESSFUL_GET_ORDER_LIST = 'orders' #флаг успешного получения заказа

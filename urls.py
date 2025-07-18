
class Url:
    MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru'

    LOGIN_COURIER = f'{MAIN_PAGE}/api/v1/courier/login'
    CREATE_COURIER = f'{MAIN_PAGE}/api/v1/courier'
    DELETE_COURIER = f'{MAIN_PAGE}/api/v1/courier/'

    CREATE_ORDER = f'{MAIN_PAGE}/api/v1/orders'
    GET_LIST_ORDERS = f'{MAIN_PAGE}/api/v1/orders'
    ORDER_CANCEL = f'{MAIN_PAGE}/api/v1/orders/cancel?track='
    TRACK_ORDER = f'{MAIN_PAGE}/api/v1/orders/track?t='

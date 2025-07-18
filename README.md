Sprint_7

test_create_courier.py       Тесты создания курьеров
test_create_courier_success	Успешная регистрация нового курьера
test_create_courier_duplicate_courier_return_error	Ошибка при повторной регистрации существующего курьера
test_create_courier_without_login_or_password_return_error	Ошибка при отсутствии логина или пароля (параметризация)


test_login_courier.py        Тесты авторизации курьеров
test_login_courier_successful	Успешная авторизация существующего курьера
test_login_courier_without_registration_return_error	Ошибка при попытке входа несуществующего курьера
test_login_courier_without_login_or_password_return_error	Ошибка при отсутствии логина или пароля (параметризация)


test_create_order.py         Тесты создания заказов
test_create_order_with_color_successful	Успешное создание заказа с разными вариантами цвета (параметризация)


test_get_order_list.py       Тесты получения листа заказов
test_get_order_list_successful Успешное получение списка заказов


generators.py Генерация тестовый данных
generate_login() – случайный логин
generate_password() – случайный пароль
generate_name() – случайное имя


urls.py Эндпоинты api

data.py Тестовые данные и ожидаемые ответы
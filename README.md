# RussCarton_AT_python
Автотесты для сайта интернет-магазина https://spb.russcarton.ru на python

Страница регистрации авторизации
1) загрузка станицы с доступной кнопкой профиля пользователя (test_check_profile_menu)
2) проверка перехода на страница профиля пользователя (test_check_going_profile_page)
3) проверка авторизации (test_authentication_user)
    Тест при выполнении вызывает проверку регистрации (test_registration_new_user), 
    получает из него сгененрированные тестовые данные и используетих для проверки авторизации.
4) проверка добавления в корзину максимально допустимого количества товара, 
    что есть в наличии (test_order_an_available_quntity)
5) проверка добавления в корзину товара, 
    больше допустимого по количеству (test_order_an_unavailable_quntity)
6) проверка добавления в корзину 0( либо отрицательного) количества товара (test_order_an_null_quntity)
7) проверка работы фильтра в категорории товаров (test_filters_on_category)
8) проверка работы поиска по названию товара (test_search_by_part_of_names)
9) проверка работы поиска по артикулу (test_search_by_part_of_number_article)
11) добавление в избранное с проверкой (test_add_products_to_favorite)

pytest -s -v --alluredir=allure-results

allure serve allure-results

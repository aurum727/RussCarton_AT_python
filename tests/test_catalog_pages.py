from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException
from pages.catalog_pages import CatalogPage
from pages.basket_page import BasketPage
from locators.catalog_page_locators import CatalogPageLocators
from locators.basket_page_locators import BasketPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TestCatalogPage:

    @pytest.fixture
    @allure.title('Создание заказа из каталога')
    @allure.description('Загружаем страницу каталога. '
                        'Получаем доступное количество товара.'
                        'Создаем заказ из первой позиции в каталоге.')
    def make_order_from_catalog(self, driver, logger, request):
        # Получаем параметр из ключа в request (если передано)
        order_balance_param = request.param if hasattr(request, 'param') else None
        catalog_page = CatalogPage(driver)
        with allure.step(f'Загружена страница каталога товаров {catalog_page.get_current_url()}'):
            catalog_page.wait_for_load_page()
            logger.info(f'загружена страница {catalog_page.get_current_url()}')
        with allure.step(f'Выбрана категория товаров "Картонные коробки от производителя"'):
            catalog_page.click_on_element(CatalogPageLocators.KARTON_BOX_ITEM)
            logger.info(f'Выбрана категория товаров "Картонные коробки от производителя"')
        with allure.step(f'Получили название товара и максимально доступное количество"'):
            item_name = catalog_page.get_text_from_element(CatalogPageLocators.FIRST_CATEGORY_ITEM_NAME)
            # получаем максимально доступное количество из карторчки товара
            item_balance = catalog_page.get_text_from_element(CatalogPageLocators.FIRST_CATEGORY_ITEM_BALANCE)
            item_balance = item_balance.replace(' в наличии', '')
            # если параметры переданы в функцию, изменяем order_balance(переменная количества заказа)
            if not order_balance_param:
                order_balance = item_balance
            else:
                if order_balance_param == 'over':
                    order_balance = str(int(item_balance) + 1)
                else:
                    order_balance = str(order_balance_param)
            logger.info(f'Название товара в каталоге: {item_name}')
            logger.info(f'Максимальное количесвтво товара доступное к заказу: {item_balance}')
        with allure.step(f'Очищено поле ввода количества товара для заказа'):
            logger.info('Очищаем поле ввода количества товара для заказа')
            catalog_page.click_on_element(CatalogPageLocators.FIRST_CATEGORY_ITEM_QUANTITY_FIELD)
            actions = ActionChains(driver)
            actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
            actions.send_keys(Keys.DELETE).perform()
            logger.info('Очищено поле ввода количества товара для заказа')
        with allure.step(f'Поле ввода количества товаров для заказа заполнено значением {order_balance}'):
            logger.info(f'Вводим в поле количество товара для заказа {order_balance}')
            catalog_page.set_text_to_field(CatalogPageLocators.FIRST_CATEGORY_ITEM_QUANTITY_FIELD, order_balance)
        with allure.step(f'Перешли на страницу корзины'):
            logger.info('Нажимаем кнопку перехода в корзину. Обрабатываем POPUP окно')
            catalog_page.click_on_element(CatalogPageLocators.FIRST_CATEGORY_ITEM_CART_BUTTON)
            if order_balance_param != 'over':
                catalog_page.wait_for_clickable_element(CatalogPageLocators.ORDER_POPUP_CART_BUTTON)
                catalog_page.click_on_element(CatalogPageLocators.ORDER_POPUP_CART_BUTTON)
        return {'item_name': item_name, 'item_balance': item_balance}

    @allure.title('Проверка заказа максимально допустимого количества товара.')
    @allure.description('Загружаем каталог товаров. Выбираем первую категорию товаров и первый товар в категории.'
                        'Получаем название товара и доступное к заказу количество.'
                        'Заказываем максимальное количество. Добавляем в корзину.'
                        'Проверяем соответствие товара и количества в корзине.')
    def test_order_an_available_quntity(self, driver, logger, make_order_from_catalog):  # pytest injects the `driver` fixture
        basket_page = BasketPage(driver)
        logger.info(f'Загружена страница {basket_page.get_current_url()}')
        with allure.step(f'На странице корзины получены значения названия товара и кличества в заказе'):
            product_name = basket_page.get_text_from_element(BasketPageLocators.get_name_product_by_position_number(1))
            logger.info(f'Название товара в корзине: {product_name}')
            product_quantity = basket_page.get_value(BasketPageLocators.get_quantity_product_by_position_number(1))
            logger.info(f'Количество товара в корзине: {product_quantity}')
        with allure.step('Товары и количество в корзине совпадают с заказом'):
            assert make_order_from_catalog['item_name'] == product_name, \
                "Название товаров в каталоге и в корзине не совпадают"
            assert make_order_from_catalog['item_balance'] == product_quantity, \
                "количество товаров указанных при заказе и в корзине не совпадает"
        basket_page.allure_screen()


    @pytest.mark.parametrize('make_order_from_catalog', ['over'], indirect=True)
    @allure.title('Проверка заказа количества товара большего, чем доступно к заказу.')
    @allure.description('Загружаем каталог товаров. Выбираем первую категорию товаров и первый товар в категории.'
                        'Получаем название товара и доступное к заказу количество.'
                        'Заказываем количество, большее чем доступно на сайте.'
                        'Получаем сообщение о превышении допустимого количества.')
    def test_order_an_unavailable_quntity(self, driver, logger, make_order_from_catalog):
        catalog_page = CatalogPage(driver)
        with allure.step(f'На странице корзины получены значения названия товара и кличества в заказе'):
            catalog_page.wait_for_invisibility_element(CatalogPageLocators.ORDER_POPUP_ERROR_MSG)
            msg = catalog_page.get_text_from_element(CatalogPageLocators.ORDER_POPUP_ERROR_MSG)
            logger.info(f'Получено сообщение "{msg}"')
        with allure.step(f'Получено сообщение о недостаточности товара на складе.'):
            assert msg == 'Необходимого количества товара нет в наличии', \
                "Отсутсвует сообщение о превышении допустимого количества товара"
        catalog_page.allure_screen()

    @pytest.mark.parametrize('make_order_from_catalog', ['0', '-1'], indirect=True)
    @allure.title('Проверка заказа нулевого/отрицательного количества товара.')
    @allure.description('Указываем в заказе ноль шт.')
    def test_order_an_null_quntity(self, driver, logger, make_order_from_catalog):  # pytest injects the `driver` fixture
        basket_page = BasketPage(driver)
        with allure.step('На странице корзины получены значения названия товара и кличества в заказе'):
            logger.info(f'Загружена страница {basket_page.get_current_url()}')
            product_name = basket_page.get_text_from_element(BasketPageLocators.get_name_product_by_position_number(1))
            logger.info(f'Название товара в корзине: {product_name}')
            product_quantity = basket_page.get_value(BasketPageLocators.get_quantity_product_by_position_number(1))
            logger.info(f'Количество товара в корзине: {product_quantity}')
        with allure.step('На странице корзины получены значения названия товара и кличества в заказе'):
            assert make_order_from_catalog['item_name'] == product_name, \
                "Название товаров в каталоге и в корзине не совпадают"
            assert '1' == product_quantity, \
                "При выборе нулевого количества товара, система указала в корзине количество отличное от 1"
        basket_page.allure_screen()

    @allure.title('Проверка работы фильтров в категории товаров в каталоге')
    @allure.description('Загружаем каталог товаров. Выбираем категорию товаров "гофрокартон".'
                        'В каждом из фильтров выставляем критериии фильтрации. Нажимаем применить.')
    def test_filters_on_category(self, driver, logger):
        catalog_page = CatalogPage(driver)
        with allure.step('На странице каталога товаров выполнен переход в категорию "Гофрокартон"'):
            catalog_page.wait_for_load_page()
            catalog_page.click_on_element(CatalogPageLocators.GOFROKARTON_ITEM)
            filters = catalog_page.get_elements(CatalogPageLocators.FILTER_ITEMS_LIST)
        with allure.step('Установлены первые пять фильтров (ползунки или чек-боксы)'):
            for filter_item in filters[:4]: # проходим только первые 4 фильтра сверху
                filter_item.find_element(*CatalogPageLocators.FILTER_TITLE).click()
                try:
                    action = ActionChains(driver)
                    slider = filter_item.find_element(*CatalogPageLocators.FILTER_SLIDER)
                    action.click_and_hold(slider).move_by_offset(200, 0).release().perform()
                except NoSuchElementException:
                    print('Элемент слайдер отсутствует в данном фильтре')

                try:
                    filter_item.find_element(*CatalogPageLocators.FILTER_ITEM_FIRST_CHECKBOX).click()
                except NoSuchElementException:
                    print('Элемент чекбокс отсутствует в данном фильтре')
        with allure.step('Выполнен поиск по заданным критериям'):
            catalog_page.click_on_element(CatalogPageLocators.FILTER_APPLY_KEY)
            filter_result_list = catalog_page.get_elements(CatalogPageLocators.FILTER_RESULT_ITEMS_LIST)
        with allure.step('Результаты фильтрации соответствуют заданным критериям.'):
            for result in filter_result_list:
                assert result.text in ['Гофрокартон листовой 2500х1250 мм, Т-24 бурый',
                                       'Гофрокартон 1250х2500 мм, Т-23 бурый'], \
                    f"{result.text} отсутствует среди допустимых значений"
        catalog_page.allure_screen()

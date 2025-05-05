import pytest
import allure

from pages.main_page import MainPage
from pages.search_page import SearchPage
from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import MainPageLocators
from locators.search_page_locators import SearchPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class TestSearchPage:

    @pytest.fixture
    @allure.title('Создание заказа из каталога')
    @allure.description('Загружаем страницу каталога. '
                        'Получаем доступное количество товара.'
                        'Создаем заказ из первой позиции в каталоге.')
    def get_search(self, driver, logger, request):
        # Получаем параметр из ключа в request (если передано)
        search_data = request.param if hasattr(request, 'param') else None
        """Метод для загрузки главной страницы, ввода поискового запроса и запуска поиска"""
        main_page = MainPage(driver)
        main_page.wait_for_load_page()
        main_page.click_on_element(MainPageLocators.SEARCH_FIELD)
        main_page.set_text_to_field(MainPageLocators.SEARCH_FIELD, search_data)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER).perform()
        return search_data

    @pytest.mark.parametrize('get_search', ['картон'], indirect=True)
    @allure.title('Проверка поиска по части названия товара.')
    @allure.description('Загружаем страницу AdressSite.main_page.'
                        'В поле поиска вводим часть названия товара "картон". Загружается страница результатов поиска.')
    def test_search_by_part_of_names(self, driver, logger, get_search):
        search_query = get_search
        count_rights_items = 0
        search_page = SearchPage(driver)
        with allure.step('Загружена страница результатов поиска'):
            search_page.wait_for_invisibility_element(SearchPageLocators.RESULT_ITEMS_NAMES_LIST)
            items = search_page.get_elements(SearchPageLocators.RESULT_ITEMS_NAMES_LIST)
        with allure.step("Проверяем, что в результатах поиска по именам позиций есть соответсвующие критериям запроса"
                    "Считаем количество позиций соответсвующих запросу."):
            for item in items:
                if search_query in (item.get_attribute('innerHTML')).lower():
                    count_rights_items += 1
            logger.info(f'Количество {count_rights_items}')
            count_rights_percent = int(count_rights_items*100/len(items))
            logger.info(f'поисковый запрос "{search_query}"')
            logger.info(f'процент верных результатов  {count_rights_percent}')
        with allure.step(f"В результатах запроса {count_rights_percent}% верных результатов, "
                         f"что соответствует допустимому (95%)."):
            assert count_rights_percent > 95, "Менее 95% записей соответствующих поисковому запросу."
        search_page.allure_screen()

    @pytest.mark.parametrize('get_search', ['артикул 10225'], indirect=True)
    @allure.title('Проверка поиска по артикулу товара.')
    @allure.description('Загружаем страницу AdressSite.main_page.'
                        'В поле поиска вводим артикул. Загружается страница результатов поиска.')
    def test_search_by_part_of_number_article(self, driver, logger, get_search):  # pytest injects the `driver` fixture
        search_query = get_search
        count_rights_items = 0
        search_page = SearchPage(driver)
        with allure.step('Загружена страница результатов поиска'):
            search_page.wait_for_invisibility_element(SearchPageLocators.RESULT_ITEMS_ARTICLES_LIST)
            items = search_page.get_elements(SearchPageLocators.RESULT_ITEMS_ARTICLES_LIST)

        with allure.step("Проверяем, что в результатах поиска по артикулам есть соответсвующие критериям запроса."
                    "Считаем количество позиций соответсвующих запросу."):
            for item in items:
                if search_query in (item.get_attribute('innerHTML')).lower():
                    count_rights_items += 1
            count_rights_percent = int(count_rights_items*100/len(items))
            logger.info(f'поисковый запрос "{search_query}"')
            logger.info(f'процент верных результатов {count_rights_percent}')
        with allure.step(f"В результатах запроса {count_rights_percent}% верных результатов, "
                         f"что соответствует допустимому (100%)."):
            assert count_rights_percent == 100, "100% записей соответствующих поисковому запросу"
        search_page.allure_screen()

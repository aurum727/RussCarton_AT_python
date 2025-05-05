import allure

import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from urls import AdressSite


class TestMainPage:

    @allure.title('Проверка загрузки главной страницы сайта. Загрузки логотипа в области footer. '
                  'Проверка доступности в меню "Профиль пользователя" возможности Входа и Регистрации на сайте')
    @allure.description('Загружаем страницу AdressSite.main_page, проверяем Логотип сайта в нижней части страницы.'
                        'В меню профиля пользователя проверяем кнопки Вход и Регистрация')
    def test_check_profile_menu(self, driver, logger):  # pytest injects the `driver` fixture
        main_page = MainPage(driver)
        main_page.wait_for_load_page()
        logger.info("Главная страница загружена")
        with allure.step('Получен список доступных операций в меню профиля'):
            main_page.get_profile_menu_items()
            items_list = main_page.get_profile_menu_items()
            logger.info(f"Доступные пункты в меню пользователя: {items_list}")
            assert set(items_list) == {'Регистрация', 'Вход'}
        main_page.allure_screen()

    @allure.title('Проверка перехода на страницу Профиля при нажатии на кнопку "Профиль"')
    @allure.description('Загружаем страницу AdressSite.main_page, проверяем Логотип сайта в нижней части страницы.'
                        'Нажимаем на кнопку профиля пользователя. Выполняем проверку URL загруженной страницы.')
    def test_check_going_profile_page(self, driver, logger):  # pytest injects the `driver` fixture
        main_page = MainPage(driver)
        main_page.wait_for_load_page()
        logger.info("Главная страница загружена")
        with allure.step('Выполнен переход на станицу профиля пользователя'):
            main_page.click_on_element(MainPageLocators.PERSONAL_PAGE_LINK)
            new_url = main_page.driver.current_url
            logger.info(f"Выполнен переход на страницу {new_url}")
            assert new_url == AdressSite.personal_page
        main_page.allure_screen()

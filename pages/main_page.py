import allure
from pages.base_page import Base
from urls import AdressSite
from locators.main_page_locators import MainPageLocators


class MainPage(Base):

    @allure.step('Ожидаем загрузку страницы')
    def wait_for_load_page(self):
        self.driver.get(AdressSite.main_page)
        self.wait_for_clickable_element(MainPageLocators.TITLE_IMAGE)
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Получаем список элементов в меню профиля пользователя')
    def get_profile_menu_items(self):
        self.wait_for_clickable_element(MainPageLocators.HEADER_PROFILE_BUTTON)
        profile_items = self.driver.find_elements(*MainPageLocators.HEADER_PROFILE_MENU_ITEMS)
        items_list = [item.get_attribute('innerHTML') for item in profile_items]
        return items_list

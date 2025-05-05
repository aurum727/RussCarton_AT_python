from selenium.common import TimeoutException
import allure
from pages.base_page import Base
from urls import AdressSite
from locators.search_page_locators import SearchPageLocators


class SearchPage(Base):

    @allure.step('Ожидаем загрузку страницы')
    def wait_for_load_page(self):
        if AdressSite.search_page not in self.driver.current_url:
            self.driver.get(AdressSite.search_page)
        self.wait_for_invisibility_element(SearchPageLocators.PAGE_TITLE_LABEL)
        try:
            self.click_on_element(SearchPageLocators.COOKIE_BUTTON)
        except TimeoutException:
            print("Cookie-уведомление не найдено, пропускаем...")
            raise

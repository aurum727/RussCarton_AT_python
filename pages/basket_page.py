from selenium.common import TimeoutException
import allure
from pages.base_page import Base
from urls import AdressSite
from locators.basket_page_locators import BasketPageLocators


class BasketPage(Base):

    @allure.step('Ожидаем загрузку страницы')
    def wait_for_load_page(self):
        if self.driver.current_url != AdressSite.basket_page:
            self.driver.get(AdressSite.basket_page)
        self.wait_for_invisibility_element(BasketPageLocators.BASKET_TITLE_LABEL)
        try:
            self.click_on_element(BasketPageLocators.COOKIE_BUTTON)
        except TimeoutException:
            print("Cookie-уведомление не найдено, пропускаем...")

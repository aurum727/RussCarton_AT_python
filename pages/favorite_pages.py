from selenium.common import TimeoutException
import allure
from pages.base_page import Base
from urls import AdressSite
from locators.favorite_page_locators import FavoritePageLocators


class FavoritePage(Base):

    @allure.step('Ожидаем загрузку страницы')
    def wait_for_load_page(self):
        if AdressSite.favorite_page not in self.driver.current_url:
            self.driver.get(AdressSite.favorite_page)
        self.wait_for_invisibility_element(FavoritePageLocators.FAVORITE_TITLE_LABEL)
        try:
            self.click_on_element(FavoritePageLocators.FAVORITE_TITLE_LABEL)
        except TimeoutException:
            print("Cookie-уведомление не найдено, пропускаем...")

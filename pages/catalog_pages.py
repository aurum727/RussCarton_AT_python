from selenium.common import TimeoutException

from pages.base_page import Base
from urls import AdressSite
from locators.catalog_page_locators import CatalogPageLocators


class CatalogPage(Base):

    def wait_for_load_page(self):
        if AdressSite.catalog_page not in self.driver.current_url:
            self.driver.get(AdressSite.catalog_page)
        self.wait_for_invisibility_element(CatalogPageLocators.CATALOG_TITLE_LABEL)
        try:
            self.click_on_element(CatalogPageLocators.COOKIE_BUTTON)
        except TimeoutException:
            print("Cookie-уведомление не найдено, пропускаем...")

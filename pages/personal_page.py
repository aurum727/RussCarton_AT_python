import allure
from pages.base_page import Base
from urls import AdressSite
from locators.personal_page_locators import PersonalPageLocators


class PersonalPage(Base):

    @allure.step('Ожидаем загрузку страницы')
    def wait_for_load_page(self):
        self.driver.get(AdressSite.personal_page)
        self.wait_for_clickable_element(PersonalPageLocators.PERSONAL_PAGE_LABEL)
        self.click_on_element(PersonalPageLocators.COOKIE_BUTTON)

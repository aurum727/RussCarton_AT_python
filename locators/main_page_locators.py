from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class MainPageLocators(BaseLocators):

    PERSONAL_PAGE_LINK = By.XPATH, '//a[@href="/personal/"]'
    HEADER_PROFILE_BUTTON = By.XPATH, '//div[@id="header__top"]//div[@class="header-profile"]'
    HEADER_PROFILE_MENU_ITEMS = By.XPATH, '//div[@id="header__top"]//ul[@class="header-profile-drop__list"]//a'
    TITLE_IMAGE = By.XPATH, '//div[@class="footer__top_logo"]'
    SEARCH_FIELD = By.XPATH, '//div[@id="smart-title-search"]//input[@type="text"]'


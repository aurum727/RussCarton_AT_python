from selenium.webdriver.common.by import By


class BaseLocators:

    PERSONAL_PAGE_LABEL = By.XPATH, '//div[@class="page-auth__login"]//div[@class="oes-modal__title"]'
    LOGIN_BUTTON_DESKTOP = By.XPATH, '//div[@class="page-auth__login"]//input[@name="Login"]'
    REGISTRATION_BUTTON_DESKTOP = By.XPATH, '//div[@class="page-auth__login"]//button[@data-modal="#modal-reg"]'
    COOKIE_BUTTON = By.XPATH, '//button[@id="cookie_accept"]'



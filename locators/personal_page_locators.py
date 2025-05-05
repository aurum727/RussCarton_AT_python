from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class PersonalPageLocators(BaseLocators):

    REGISTRATION_LABEL_MODAL = By.XPATH, '//div[@class="oes-modal opened"]//div[@class="oes-modal__title"]'
    FIO_TEXTFIELD = By.XPATH, '//input[@name="UF_USER_FULL_NAME"]'
    EMAIL_TEXTFIELD = By.XPATH, '//input[@name="REGISTER[EMAIL]"]'
    PHONE_TEXTFIELD = By.XPATH, '//input[@name="REGISTER[PERSONAL_PHONE]"]'
    PASSWORD_TEXTFIELD = By.XPATH, '//input[@name="REGISTER[PASSWORD]"]'
    PASSWORD_CONFIRM_TEXTFIELD = By.XPATH, '//input[@name="REGISTER[CONFIRM_PASSWORD]"]'
    PRIVATE_USER_RADIO_BUTTON = By.XPATH, '//span[text()="Я частное лицо"]'
    MAKE_REGISTRATION_KEY = By.XPATH, '//div[@class="oes-modal opened"]//input[@name="register_submit_button"]'
    PERSONAL_NAME_LABEL = By.XPATH, '//main[@class="cabinet__content"]//span[text()="ФИО"]/parent::li/span[2]'

    AUTH_EMAIL_TEXTFIELD = By.XPATH, '//div[@class="page-auth__login"]//input[@name="USER_LOGIN"]'
    AUTH_PASSWORD_TEXTFIELD = By.XPATH, '//div[@class="page-auth__login"]//input[@name="USER_PASSWORD"]'
    AUTH_ENTER_KEY = By.XPATH, '//div[@class="page-auth__login"]//input[@name="Login"]'


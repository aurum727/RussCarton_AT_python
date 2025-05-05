import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Нажимаем на элемент с локатором {element_locator}')
    def click_on_element(self, element_locator):
        self.driver.find_element(*element_locator).click()

    @allure.step('Заполняем поле {element_locator} текстом {text}')
    def set_text_to_field(self, element_locator, text):
        self.driver.find_element(*element_locator).send_keys(text)

    @allure.step('Скролим страницу для элемента {element_locator}')
    def move_to_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем кликабельного элемента {element_locator}')
    def wait_for_clickable_element(self, element_locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable((element_locator)))
        return wait

    @allure.step('Ожидаем видимого элемента {element_locator}')
    def wait_for_invisibility_element(self, element_locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((element_locator)))
        return wait

    @allure.step('Сохраняем скриншот')
    def make_screenshot(self):
        now_date = datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
        name_screenshot = "screen " + now_date + ".png"
        self.driver.save_screenshot(f"screen/{name_screenshot}")

    def allure_screen(self):
        now_date = datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
        screenshot_png = "screen " + now_date + ".png"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=screenshot_png,
                      attachment_type=AttachmentType.PNG)

    @allure.step('Читаем надпись в элементе {element_locator}')
    def get_text_from_element(self, element_locator):
        return self.driver.find_element(*element_locator).text

    def get_elements(self, elements_locator):
        return self.driver.find_elements(*elements_locator)

    @allure.step('Обновляем сессию браузера')
    def refresh_session(self):
        self.driver.delete_all_cookies()

    @allure.step('Очищаем поле ввода {element_locator}')
    def clear_textfield(self, element_locator):
        textfield = self.driver.find_element(*element_locator)
        textfield.clear()

    @allure.step('Получаем значение из элемента {element_locator}')
    def get_value(self, element_locator):
        return self.driver.find_element(*element_locator).get_attribute('value')

    @allure.step('Вводим данные в элемент {element_locator} {Keys}')
    def send_key(self, element_locator, Keys):
        self.driver.find_element(*element_locator).send_keys(Keys)


from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class BasketPageLocators(BaseLocators):

    BASKET_TITLE_LABEL = By.XPATH, '//h1[@class="page__title-h2"]'
    FIRST_ITEM_NAME_LABEL = By.XPATH, '(//div[@class="product__td__dsc"]/a)[1]'
    FIRST_ITEM_QUANTITY_INPUT = By.XPATH, '(//td//div[@class="quantity"]/input[@type="text"])[1]'


    @staticmethod
    def get_name_product_by_position_number(position_number):
        NAME_PRODUCT_BY_POSITION_NUMBER = By.XPATH, f'(//div[@class="product__td__dsc"]/a)[{str(position_number)}]'
        return NAME_PRODUCT_BY_POSITION_NUMBER

    @staticmethod
    def get_quantity_product_by_position_number(position_number):
        NAME_QUANTITY_BY_POSITION_NUMBER = \
            By.XPATH, f'(//td//div[@class="quantity"]/input[@type="text"])[{str(position_number)}]'
        return NAME_QUANTITY_BY_POSITION_NUMBER

from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class FavoritePageLocators(BaseLocators):

    FAVORITE_TITLE_LABEL = By.XPATH, '//h1[@class="page_content__title"]'
    PRODUCTS_NAMES_LIST = By.XPATH, '//div[@class="popular__product_item-name"]/a'

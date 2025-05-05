from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class SearchPageLocators(BaseLocators):
    PAGE_TITLE_LABEL = By.XPATH, '//h1[@class="page_content__title" and contains(text(), "поиск")]'
    SEARCH_FIELD = By.XPATH, '//div[@class="search-page"]//input[@type="text"]'
    RESULT_ITEMS_NAMES_LIST = By.XPATH, '//div[@class="popular__product_item-name"]/a[contains(@href,"/catalog")]'
    RESULT_ITEMS_ARTICLES_LIST = By.XPATH, '//div[@class="popular__product-article"]'

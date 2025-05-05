from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators


class CatalogPageLocators(BaseLocators):
    CATALOG_TITLE_LABEL = By.XPATH, '//h1[@class="page_content__title" and text()="Каталог"]'
    KARTON_BOX_ITEM = By.XPATH, '//div[@class="catalog-item "]//a[text()="Картонные коробки"]'
    KARTON_BOX_PAGE_LABEL = By.XPATH, '//h1[@class="page_content__title"]'
    FIRST_CATEGORY_ITEM_NAME = By.XPATH, '(//div[@class="popular__product_item-name"]/a)[1]'
    FIRST_CATEGORY_ITEM_BALANCE = By.XPATH, '(//div[@class="warehouses__val warehouses__val_yes"])[1]'
    FIRST_CATEGORY_ITEM_QUANTITY_FIELD = \
        By.XPATH, '(//div[@class="popular__product_presence"])[1]//input[@type="number"]'
    FIRST_CATEGORY_ITEM_CART_BUTTON = By.XPATH, '(//div[@class="popular__product_btn"])[1]//a[@class="btn_card pop"]'
    ORDER_POPUP_CART_BUTTON = By.XPATH, '//div[@class="mfp-content"]//a[@class="btn_card"]'
    ORDER_POPUP_UNAVAILABLE_MSG = By.XPATH, '//div[@class="mfp-content"]//span'  # Необходимого количества товара нет в наличии
    ORDER_POPUP_ERROR_MSG = By.XPATH, '//div[@id="popup_addbasket_error"]//div[@class="title_popup"]/span'

    # FILTERS ON CATEGORY
    GOFROKARTON_ITEM = By.XPATH, '//div[@class="catalog-item "]//a[text()="Гофрокартон"]'
    FILTER_ITEMS_LIST = By.XPATH, '//div[@class="bx_filter_parameters_box "]'
    FILTER_TITLE = By.XPATH, './/div[@class="bx_filter_parameters_box_title"]'
    FILTER_SLIDER = By.XPATH, './/a[@class="bx_ui_slider_handle left"]'
    FILTER_ITEM_FIRST_CHECKBOX = By.XPATH, './/label[@class="bx_filter_param_label"]'
    FILTER_APPLY_KEY = By.XPATH, '//input[@class="bx_filter_search_button"]'
    FILTER_RESULT_ITEMS_LIST = By.XPATH, '//div[@class="popular__product_item-name"]//a'

    PRODUCT_ITEMS = By.XPATH, '//div[@class="popular__product_item_info"]'
    PRODUCT_ITEM_NAME = By.XPATH, './/div[@class="popular__product_item-name"]//a'
    PRODUCT_ITEM_FAVORITE_BUTTONS = By.XPATH, \
                                    './/div[@class="product-cart__favorites-btn product-cart__favorites-btn_detail"]'

    HEADER_FAVORITE_BUTTON = By.XPATH, '//div[@class="header__favorites in"]'

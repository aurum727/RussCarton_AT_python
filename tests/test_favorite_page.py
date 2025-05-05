import allure
import pytest
from locators.catalog_page_locators import CatalogPageLocators
from locators.favorite_page_locators import FavoritePageLocators
from pages.catalog_pages import CatalogPage
from pages.favorite_pages import FavoritePage


class TestFavoritesPage:

    @allure.title('Проверка добавления товара в избранное.')
    @allure.description('Загружаем страницу AdressSite.main_page.'
                        'На главной странице выбираем первую категорию товаров.'
                        'Добавляем первые два товара в избранное.'
                        'Переходим в избранное.'
                        'Проверяем наличие товаров в избранном.')
    def test_add_products_to_favorite(self, driver, logger):
        product_names = []
        catalog_page = CatalogPage(driver)
        catalog_page.wait_for_load_page()
        logger.info(f'загружена страница {catalog_page.get_current_url()}')
        with allure.step('Переходим на страницу "Картонные коробки"'):
            catalog_page.click_on_element(CatalogPageLocators.KARTON_BOX_ITEM)
        with allure.step('Первые пять позиций в категории добавляем "Избранное"'):
            product_items = catalog_page.get_elements(CatalogPageLocators.PRODUCT_ITEMS)
            for item in product_items[:5]:
                item_name = item.find_element(*CatalogPageLocators.PRODUCT_ITEM_NAME).text
                product_names.append(item_name)
                logger.info(f'{item_name} добавлен в избранное')
                item.find_element(*CatalogPageLocators.PRODUCT_ITEM_FAVORITE_BUTTONS).click()
        logger.info('Переходим на страницу раздела избранного')
        with allure.step('Переходим на страницу "Избранное"'):
            catalog_page.click_on_element(CatalogPageLocators.HEADER_FAVORITE_BUTTON)
            favorite_page = FavoritePage(driver)
            favorite_page.wait_for_load_page()
        with allure.step('Все товары добавленные в избранное присутствуют на странице избранное'):
            favorites_products_list = favorite_page.get_elements(FavoritePageLocators.PRODUCTS_NAMES_LIST)
            for favorite_product in favorites_products_list:
                assert favorite_product.text in product_names, "Товар ошибочно присутствует в избранном."
                logger.info(f'{favorite_product.text} присутвует в избранном')
        catalog_page.allure_screen()

import allure
import pytest

from locators.personal_page_locators import PersonalPageLocators
from pages.personal_page import PersonalPage
from utilities.fake_data_generator import FakeData


class TestPersonalPage:

    @pytest.fixture
    @allure.title('Проверка регистрации нового пользователя.')
    @allure.description('Переход на страницу пользователя. Регистрация нового пользователя.')
    def test_registration_new_user(self, driver, logger):  # pytest injects the `driver` fixture
        pytest.shared = {} # переменная для хранения значений передаваемых в зависимый тест (test_authentication_user)
        personal_page = PersonalPage(driver)
        fake = FakeData()
        personal_page.wait_for_load_page()
        logger.info("Загружена страница приглашения пользователя")
        with allure.step('Загружена форма регистрации нового пользователя'):
            # press reg button
            personal_page.click_on_element(PersonalPageLocators.REGISTRATION_BUTTON_DESKTOP)
            # load modal windows
            personal_page.wait_for_clickable_element(PersonalPageLocators.REGISTRATION_LABEL_MODAL)
        with allure.step('Заполнены поля регистрациооной формы'):
            fullname = fake.get_full_name()
            pytest.shared.update({'fullname': fullname})
            personal_page.set_text_to_field(PersonalPageLocators.FIO_TEXTFIELD, fullname)
            logger.info(f"Регистрируется пользователь {fullname}")
            email = fake.get_email()
            personal_page.set_text_to_field(PersonalPageLocators.EMAIL_TEXTFIELD, email)
            logger.info(f"Регистрируется пользователь {email}")
            personal_page.set_text_to_field(PersonalPageLocators.PHONE_TEXTFIELD, fake.get_phone_number())
            personal_page.set_text_to_field(PersonalPageLocators.PASSWORD_TEXTFIELD, "Pa$$w0rd123")
            personal_page.set_text_to_field(PersonalPageLocators.PASSWORD_CONFIRM_TEXTFIELD, "Pa$$w0rd123")
            personal_page.click_on_element(PersonalPageLocators.PRIVATE_USER_RADIO_BUTTON)
            personal_page.click_on_element(PersonalPageLocators.MAKE_REGISTRATION_KEY)
        with allure.step('Загружена страница профиля нового пользователя'):
            logger.info(f"Нажата кнопка регистрации нового пользователя")
            personal_page.wait_for_invisibility_element(PersonalPageLocators.PERSONAL_NAME_LABEL)
            logger.info("Загрузилась страница профиля нового вользователя")
            fio_profile = personal_page.get_text_from_element(PersonalPageLocators.PERSONAL_NAME_LABEL)
            logger.info(f"На странице пользователя отображается имя {fio_profile}")
            assert fullname == fio_profile, "ФИО нового пользователя не совпаает с заданным при регистрации"
            logger.info("Успешно создан новый пользователь")
            personal_page.allure_screen()
        return {'email': email, 'password': 'Pa$$w0rd123', 'fullname': fullname, 'page_object': personal_page}

    @allure.title('Проверка регистрации нового пользователя.')
    @allure.description('Переход на страницу пользователя. Регистрация нового пользователя.')
    def test_authentication_user(self, driver, logger, test_registration_new_user):  # pytest injects the `driver` fixture
        logger.info("Попытка авторизации новым пользователем")
        personal_page = test_registration_new_user['page_object']
        email = test_registration_new_user['email']
        password = test_registration_new_user['password']
        fullname = test_registration_new_user['fullname']
        with allure.step(f'Очищены куки. Обновлена страница профиля пользователя.'):
            personal_page.refresh_session()
            logger.info("Очищаем сессию браузера. Обновляем страницу")
            personal_page.wait_for_load_page()
            logger.info("Загружена страница профиля пользователя")
        with allure.step(f'Заполнены поля формы авторизации'):
            personal_page.set_text_to_field(PersonalPageLocators.AUTH_EMAIL_TEXTFIELD, email)
            personal_page.set_text_to_field(PersonalPageLocators.AUTH_PASSWORD_TEXTFIELD, password)
        with allure.step('Выполнен вход. Загружена страница профиля пользователя.'):
            personal_page.click_on_element(PersonalPageLocators.AUTH_ENTER_KEY)
            logger.info("Выполняем вход в профиль нового пользователя")
            personal_page.wait_for_invisibility_element(PersonalPageLocators.PERSONAL_NAME_LABEL)
            logger.info("Загрузилась страница профиля нового вользователя")
        with allure.step('В профлие пользователя отображается ФИО пользователя.'):
            fio_profile = personal_page.get_text_from_element(PersonalPageLocators.PERSONAL_NAME_LABEL)
            logger.info(f"На странице пользователя отображается имя {fio_profile}")
            assert fullname == fio_profile, "ФИО пользователя в профиле не совпадается с заданными при регистрации"
            logger.info(f"Имя нового пользователя совпадает с именем в профиле")
        personal_page.allure_screen()

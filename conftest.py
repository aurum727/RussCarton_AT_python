import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import logging
import os
from datetime import datetime


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(executable_path=binary_path)
    driver = webdriver.Chrome(options=options, service=g)
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_configure():
    # Настройка директории и файла для логов
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(log_dir, f"tests_{current_time}.log")

    # Формат логов
    log_format = '%(asctime)s | %(levelname)-8s | %(message)s'

    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup(item):
    """Логирование перед запуском теста"""
    logging.info(f"[START] Тест: {item.name}")
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item, nextitem):
    """Логирование после завершения теста"""
    yield
    logging.info(f"[END] Тест: {item.name}\n")


@pytest.fixture(scope="function")
def logger(request):
    """Фикстура для логирования внутри теста"""
    test_name = request.node.name
    log = logging.getLogger(test_name)

    # Добавляем разделитель для читаемости
    log.info(f"Тест '{test_name}' начал выполнение")

    yield log


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        if result.failed:
            logging.error(f"ТЕСТ ПРОВАЛЕН: {item.name}")
        else:
            logging.info(f"ТЕСТ ПРОЙДЕН: {item.name}")

import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    url = 'https://shop.tastycoffee.ru'

    options = webdriver.FirefoxOptions()
    # options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
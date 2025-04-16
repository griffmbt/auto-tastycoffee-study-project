from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))



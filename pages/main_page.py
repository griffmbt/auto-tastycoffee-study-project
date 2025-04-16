import time
from base.base import Base
from selenium.webdriver.common.by import By


class MainPage(Base):

        # Locators

        espresso_coffee_menu = '//b[contains(text(), "для эспрессо")]'
        modal_cookies_button = '//span[text()="Согласен"]'

        # Getters

        def get_espresso_coffee_menu(self):
            return self.wait_for_element(By.XPATH, self.espresso_coffee_menu)

        def get_modal_cookies_button(self):
            return self.wait_for_element(By.XPATH, self.modal_cookies_button)

        # Actions

        def click_espresso_coffee_menu(self):
            self.get_espresso_coffee_menu().click()
            print('меню: кофе для эспрессо выбрано')

        def click_modal_cookies_button(self):
            self.get_modal_cookies_button().click()
            print('модалка cookies убрана')

        # Methods

        def go_to_coffee_menu_for_espresso(self):
            self.click_modal_cookies_button()
            self.click_espresso_coffee_menu()




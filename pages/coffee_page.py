import time
from base.base import Base
from selenium.webdriver.common.by import By


class CoffeePage(Base):

        # Locators

        filter_medium_acidity = '//input[@id="filters-v-0-0-3-1"]'
        filter_medium_density = '//input[@id="filters-v-0-0-3-4"]'
        filter_medium_roasting = '//input[@id="filters-v-0-0-3-7"]'
        item_1_button = '(//button[@class="tc-btn-pay"])[1]'
        cart = '//div[@class="flex items-center cursor-pointer"]'
        cart_count = '//span[@class="block max-w-[80px] whitespace-nowrap overflow-hidden text-ellipsis mr-1"]'
        # h1 = 'h1'

        # Getters

        def get_filter_acidity(self):
            return self.wait_for_element(By.XPATH, self.filter_medium_acidity)

        def get_filter_density(self):
            return self.wait_for_element(By.XPATH, self.filter_medium_density)

        def get_filter_roasting(self):
            return self.wait_for_element(By.XPATH, self.filter_medium_roasting)

        def get_item_1_button(self):
            return self.wait_for_element(By.XPATH, self.item_1_button)

        def get_cart(self):
            return self.wait_for_element(By.XPATH, self.cart)

        def get_cart_count(self):
            return self.wait_for_element(By.XPATH, self.cart_count)

        # def get_h1(self):
        #     return self.wait_for_element(By.CSS_SELECTOR, self.h1)


        # Actions

        def click_filter_acidity(self):
            self.get_filter_acidity().click()
            print('выбран фильтр: средняя кислотность')

        def click_filter_density(self):
            self.get_filter_density().click()
            print('выбран фильтр: средняя плотность')

        def click_filter_roasting(self):
            self.get_filter_roasting().click()
            print('выбран фильтр: средняя обжарка')

        def click_item_1_button(self):
            self.get_item_1_button().click()
            print('товар выбран')

        def click_cart(self):
            self.get_cart().click()
            print('нажал на корзину')

        # Methods

        def add_filters(self):
            self.click_filter_acidity()
            self.click_filter_density()
            self.click_filter_roasting()

            time.sleep(3)

        def add_item_1_and_go_to_cart(self):
            self.click_item_1_button()
            self.click_cart()



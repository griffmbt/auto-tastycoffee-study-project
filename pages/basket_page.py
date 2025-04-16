import time
from faker import Faker
from base.base import Base
from selenium.webdriver.common.by import By


class BasketPage(Base):

        fake = Faker()
        full_name = fake.name()
        phone = '9062223344'
        email = fake.email()
        num = fake.random_number()
        address = 'г.Ижевск, ул. Пушкинская 273'

        # Locators

        user_full_name = '//input[@id="cart.user.full_name-v-0-0-2"]'
        user_phone = '//input[@id="cart.user.phone-v-0-0-3"]'
        user_email = '//input[@id="cart.user.email-v-0-0-5"]'
        user_address = '//input[@id="cart.address-v-0-0-12"]'
        user_flat = '//input[@id="flat-v-0-0-13"]'
        delivery_method = '//input[@id="tastycoffee.1"]'
        selection_address = '(//li[@class="cursor-pointer"])[1]'
        basket_button = '//span[contains(text(), "Оформить заказ")]'
        logo_payment_page = '//img[@alt="Сбербанк"]'


        # Getters

        def get_user_full_name(self):
            return self.wait_for_element(By.XPATH, self.user_full_name)

        def get_user_phone(self):
            return self.wait_for_element(By.XPATH, self.user_phone)

        def get_user_email(self):
            return self.wait_for_element(By.XPATH, self.user_email)

        def get_user_address(self):
            return self.wait_for_element(By.XPATH, self.user_address)

        def get_user_flat(self):
            return self.wait_for_element(By.XPATH, self.user_flat)

        def get_delivery_method(self):
            return self.wait_for_element(By.XPATH, self.delivery_method)

        def get_logo_payment_page(self):
            return self.wait_for_element(By.XPATH, self.logo_payment_page)

        def get_basket_button(self):
            return self.wait_for_element(By.XPATH, self.basket_button)

        def get_selection_address(self):
            return self.wait_for_element(By.XPATH, self.selection_address)

        # Actions

        def input_user_full_name(self, full_name):
            self.get_user_full_name().send_keys(full_name)
            print('введено ФИО')

        def input_user_phone(self, phone):
            self.get_user_phone().send_keys(phone)
            print('введен номер телефона')

        def input_user_email(self, email):
            self.get_user_email().send_keys(email)
            print('введен email')

        def input_user_address(self, address):
            self.get_user_address().send_keys(address)

        def click_selection_address(self):
            self.get_selection_address().click()
            print('введен адрес')

        def input_user_flat(self, flat):
            self.get_user_flat().send_keys(flat)
            print('введен номер квартиры')

        def click_basket_button(self):
            self.get_basket_button().click()
            print('нажата кнопка "Оформить заказ"')


        # Methods

        def submitting_form(self):
            self.input_user_full_name(self.full_name)
            self.input_user_phone(self.phone)
            self.input_user_email(self.email)
            self.get_user_address().clear()
            self.input_user_address(self.address)
            self.click_selection_address()
            self.input_user_flat(self.num)
            self.get_delivery_method()
            time.sleep(3)
            self.click_basket_button()




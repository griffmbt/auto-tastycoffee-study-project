from pages.basket_page import BasketPage
from pages.coffee_page import CoffeePage
from pages.main_page import MainPage


def test_buy_coffee(driver):
    print('Старт теста: test_add_coffee_to_cart')

    mp = MainPage(driver)
    mp.go_to_coffee_menu_for_espresso() # перешли в меню "кофе для эспрессо"

    cp = CoffeePage(driver)
    cp.add_filters()  # Применяем фильтры
    cp.add_item_1_and_go_to_cart()  # Добавляем первый товар в корзину и переходим в корзину

    # Проверка: количество товаров в корзине
    cart_count = cp.get_cart_count().text.strip()
    assert cart_count == "1", f"Ожидалось 1 товар в корзине, но было {cart_count}"

    bp = BasketPage(driver)
    bp.submitting_form()

    # Проверка: нахождения на странице оплаты
    payment_logo = bp.get_logo_payment_page().get_attribute("alt")
    assert payment_logo == "Сбербанк", f"Ожидалось лого 'Сбербанк', но было {payment_logo}"

    print('Тест пройден успешно')



from conftest import browser
from pages.swag_labs import Swag_labs


def test_icon_exist(browser):
    demo_page = Swag_labs(browser)
    demo_page.visit()
    assert demo_page.exist_icon()


def test_field_name(browser):
    demo_page = Swag_labs(browser)
    demo_page.visit()
    assert demo_page.exist_field(locator="#user-name")


def test_field_password(browser):
    demo_page = Swag_labs(browser)
    demo_page.visit()
    assert demo_page.exist_field(locator="#password")

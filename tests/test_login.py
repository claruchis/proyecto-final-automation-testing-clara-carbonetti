from selenium.webdriver.remote.webdriver import WebDriver
from page.login_page import LoginPage


def test_login_ok (driver: WebDriver):
    login_page = LoginPage(driver)
    
    login_page.login("standard_user", "secret_sauce") #datos que quiero ejecutar en el test

    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario" #validación login

def test_login_invalid_password(driver: WebDriver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "123456")

    error = login_page.get_error_password_message()

    assert "Epic sadface: Username and password do not match any user in this service" in error
    
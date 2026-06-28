#traigo a selenium y al webdriver de chrome, luego abro la pagina y por ultimo cierro el navegador
#by y keys hay que importarlos en cada archivo que los vayamos a usar, son parte de selenium.webdriver.common

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    
from selenium.webdriver.remote.webdriver import WebDriver
from page.login_page import LoginPage

from utils.logger import logger

def test_login_ok (driver: WebDriver):
    logger.info("Iniciando el driver para test_login_ok")  #log de info

    login_page = LoginPage(driver)
    
    logger.info("Ejecutando login con usuario y contraseña correctos")  #log de info
    login_page.login("standard_user", "secret_sauce") #datos que quiero ejecutar en el test

    logger.info("Iniciando sesión...")  #log de info

    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario" #validación login
    logger.info("Sesión iniciada correctamente")  #log de info

def test_login_invalid_password(driver: WebDriver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "123456")

    error = login_page.get_error_password_message()

    #assert "Epic sadface: Username and password do not match any user in this service" in error
    assert error == "hola"
    
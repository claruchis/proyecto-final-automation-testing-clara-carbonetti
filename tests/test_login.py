from selenium.webdriver.remote.webdriver import WebDriver
from page.login_page import LoginPage

from utils.logger import logger

def test_login_ok (driver: WebDriver):
    
    login_page = LoginPage(driver)
    
    login_page.login("standard_user", "secret_sauce") #datos que quiero ejecutar en el test

    if "/inventory.html" in driver.current_url:
        logger.info("Sesión iniciada correctamente")  #log de info
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario" #validación login
    
        
    

def test_login_invalid_password(driver: WebDriver):
    logger.info("Iniciando el driver para test_login_invalid_password")  #log de info
    
    login_page = LoginPage(driver)
    
    logger.info("Iniciando sesión password inválida")  #log de info
    
    login_page.login("standard_user", "123456")
    
    error = login_page.get_error_password_message()

    
    #if error == "hola":
    #    logger.info("El assert esperado se cumplió")
    #else:
    #    logger.error(f"El mensaje mostrado no coincide. Mensaje recibido: {error}")

    #assert error == "hola" #dejo este assert para que falle y se genere la captura de pantalla, el assert correcto queda comentado
   
    
    if "Epic sadface: Username and password do not match any user in this service" in error:
        logger.info("Sesión no iniciada correctamente")  #log de info
    else:
        logger.info("El mensaje mostrado no coincide")  #log de error
    
    assert "Epic sadface: Username and password do not match any user in this service" in error

    
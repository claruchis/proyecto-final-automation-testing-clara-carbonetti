from page.login_page import LoginPage
from utils.data_reader import read_users_csv
import pytest

from utils.logger import logger

@pytest.mark.parametrize("user", read_users_csv())
def test_login(driver, user):
    
    logger.info("Inciando el driver para test_login.csv")  #log de info
    
    login_page = LoginPage(driver)

    logger.info("Iniciando sesión en test_login.csv")  #log de info
    
    login_page.login(user["username"], user["password"])
    if user["valid"] == "true":
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        
    else:
        error = login_page.get_error_password_message()
        assert "Epic sadface" in error
    
    if "/inventory.html" in driver.current_url:
        logger.info("Sesión iniciada correctamente test_login_csv.py")  #log de info
    else: 
        logger.info("Sesión no iniciada correctamente test_login_csv.py")  #log de info
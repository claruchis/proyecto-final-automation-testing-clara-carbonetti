from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage   

@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    return InventoryPage(driver)  # Devuelve la instancia de InventoryPage después del inicio de sesión

def test_inventory_title(driver_logged):
    titulo = driver_logged.obtener_titulo()
    assert titulo == "Swag Labs", "El título de la página de inventario no es correcto" 
  
def test_productos_visible(driver_logged):
    productos = driver_logged.obtener_productos()
    assert len(productos) > 0, "No se encontraron productos en la página de inventario"

def test_menu_visible(driver_logged):
    assert driver_logged.menu_visible(), "El menú no está visible en la página de inventario"   

    assert driver_logged.filtro_visible(), "El filtro no está visible en la página de inventario"

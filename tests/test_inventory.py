from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage   


def test_inventory_title(driver_logged):
    inventory_page = InventoryPage(driver_logged)

    titulo = inventory_page.obtener_titulo()
    assert titulo == "Swag Labs", "El título de la página de inventario no es correcto" 
  
def test_productos_visible(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0, "No se encontraron productos en la página de inventario"

def test_menu_visible(driver_logged):
    inventory_page = InventoryPage(driver_logged)
    
    assert inventory_page.menu_visible(), "El menú no está visible en la página de inventario"   

    assert inventory_page.filtro_visible(), "El filtro no está visible en la página de inventario"

from page.inventory_page import InventoryPage
from utils.logger import logger


def test_inventory_title(driver_logged):
    logger.info("Iniciando test_inventory_title")
    inventory_page = InventoryPage(driver_logged)

    titulo = inventory_page.obtener_titulo()
    logger.info(f"Título obtenido: {titulo}")
    
    assert titulo == "Swag Labs", "El título de la página de inventario no es correcto"

    logger.info("Test finalizado correctamente")
  

def test_productos_visible(driver_logged):
    logger.info("Iniciando test_productos_visible")
    inventory_page = InventoryPage(driver_logged)
    
    productos = inventory_page.obtener_productos()
    logger.info(f"Productos encontrados: {len(productos)}")
    
    assert len(productos) > 0, "No se encontraron productos en la página de inventario"
    
    logger.info("Test finalizado correctamente")


def test_menu_visible(driver_logged):
    logger.info("Iniciando test_menu_visible")
    inventory_page = InventoryPage(driver_logged)
    
    menu_visible = inventory_page.menu_visible()
    logger.info(f"Estado del menú: {menu_visible}")
    
    assert menu_visible, "El menú no está visible en la página de inventario"   

    filtro_visible = inventory_page.filtro_visible()
    logger.info(f"Estado del filtro: {filtro_visible}")
   
    assert filtro_visible, "El filtro no está visible en la página de inventario"
   
    logger.info("Test finalizado correctamente")
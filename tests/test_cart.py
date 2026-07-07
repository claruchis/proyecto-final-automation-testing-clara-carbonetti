from selenium.webdriver.common.by import By
from page.cart_page import CartPage
from utils.logger import logger


def test_cart(driver_logged):
    logger.info("Iniciando test_cart")

    driver = driver_logged

    # Obtener el nombre del producto antes de agregarlo
    producto = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
    logger.info(f"Producto seleccionado: {producto}")

    # Agregar el producto
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    # Verificar contador
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    logger.info(f"Cantidad de productos en el carrito: {contador}")

    assert contador == "1", "La cantidad de productos no se agregaron correctamente"

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    logger.info("Ingresando al carrito")

    cart_page = CartPage(driver)

    productos = cart_page.obtener_productos_carrito()
    logger.info(f"Productos en el carrito: {productos}")

    assert len(productos) == 1, "El carrito debería contener un solo producto"
    assert productos[0]["nombre"] == producto, "El producto agregado no coincide"

    logger.info("Test finalizado correctamente")
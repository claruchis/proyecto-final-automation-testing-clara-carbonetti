from selenium.webdriver.common.by import By


def test_add_product_to_cart(driver_logged):

    driver = driver_logged


    # Obtener nombre del primer producto
    primer_producto = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text


    # Click en agregar al carrito
    boton = driver.find_element(
        By.CSS_SELECTOR,
        ".btn_inventory"
    )

    boton.click()


    # Verificar contador carrito = 1
    carrito = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert carrito.text == "1"


    # Entrar al carrito
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()


    # Verificar producto agregado
    producto_carrito = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text


    assert producto_carrito == primer_producto
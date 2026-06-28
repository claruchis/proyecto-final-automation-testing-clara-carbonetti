from selenium.webdriver.common.by import By


def test_inventory_page(login_in_driver):

    driver = login_in_driver


    # 1) Validar título visible
    titulo = driver.find_element(By.CLASS_NAME,"title")

    assert titulo.text == "Products"


    # 2) Verificar productos visibles
    productos = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    assert len(productos) > 0


    # 3) Obtener nombre del primer producto
    primer_nombre = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text


    # Obtener precio del primero
    primer_precio = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text


    print(
        f"\nProducto: {primer_nombre}"
    )

    print(
        f"Precio: {primer_precio}"
    )
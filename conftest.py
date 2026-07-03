import pytest
from selenium import webdriver
from page.login_page import LoginPage
from utils.data_reader import read_users_csv
import pathlib
import pytest_html


#vamos a definir todo lo q corresponde al inicio de la página

@pytest.fixture #esto funciona como una especie de variable global reutilizable en todos los test
def driver():
    options = webdriver.ChromeOptions() #se van a ejecutar las opciones del navegador 
    options.add_argument("--incognito") #con esto le digo al navegador que se abra en modo incognito

    driver = webdriver.Chrome(options=options) #con esto le digo al navegador que se abra con las opciones que definí anteriormente, el 2do options es la variable, la 1ra es el parámetro

    driver.get("https://www.saucedemo.com/")
    
    yield driver #yield es como un return pero permite que el código después de yield se ejecute después del test-> pausa el código en este punto
    
    
    driver.quit()

@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)

    user = read_users_csv()[0]  # Tomamos el primer usuario del CSV
    
    login_page.login(user["username"], user["password"])
    return driver  # Devuelve el driver después del inicio de sesión

@pytest.hookimpl(tryfirst=True, hookwrapper=True)  #va a ejecutar el código antes de que se ejecute el test, y va a envolver el test para poder ejecutar código después del test
def pytest_runtest_makereport(item, call):   #identifica diferentes estados de la prueba
    outcome = yield   #yield permite que el código después de yield se ejecute después del test
    
    report = outcome.get_result() #guarda el resultado de la prueba en la variable report

    #when puede ser setup, call o teardown. Setup es antes de ejecutar el test, call es cuando se ejecuta el test y teardown es después de ejecutar el test
    if report.when == "call" and report.failed:    
        driver = item.funcargs.get("driver")  # busco el fixture del driver

        if driver:
            target = pathlib.Path("reports/screenshots")  # Carpeta donde se guardarán las capturas de pantalla
            target.mkdir(parents=True, exist_ok=True)  # Crear la carpeta si no existe, si existe no hace nada
            
            file_name = target / f"{item.name}.png"  # Defino el nombre del archivo: nombre de la prueba

            driver.save_screenshot(str(file_name))  # Guardo la captura de pantalla y le doy el nombre del archivo (str)

            #voy a adjuntar la imagen al reporte.html en una columna que voy a agregar, antes evaluo si la puedo agregar
            if hasattr(report, "extra"):
                report.extra.append({
                    "name": "Screenshot",
                    "format": "image",
                    "content": str(file_name)

                })

            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(str(file_name)))

            report.extras = extras

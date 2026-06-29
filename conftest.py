import pytest
from selenium import webdriver
from page.login_page import LoginPage
from utils.data_reader import read_users_csv


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

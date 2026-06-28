import pytest
from selenium import webdriver
#from utils.login_page import login


#vamos a definir todo lo q corresponde al inicio de la página

@pytest.fixture #esto funciona como una especie de variable global reutilizable en todos los test
def driver():
    options = webdriver.ChromeOptions() #se van a ejecutar las opciones del navegador 
    options.add_argument("--incognito") #con esto le digo al navegador que se abra en modo incognito

    driver = webdriver.Chrome(options=options) #con esto le digo al navegador que se abra con las opciones que definí anteriormente, el 2do options es la variable, la 1ra es el parámetro

    driver.get("https://www.saucedemo.com/")
    
    yield driver #yield es como un return pero permite que el código después de yield se ejecute después del test-> pausa el código en este punto
    
    
    driver.quit()

#@pytest.fixture
#def login_in_driver(driver):
        #login(driver) #con esto llamo a la función login que definí en el archivo login_page.py 
        #yield driver #con esto devuelvo el driver para que se pueda usar en los test que lo llamen
    

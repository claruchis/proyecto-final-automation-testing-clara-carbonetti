import csv
import json

def read_users_csv():
    with open("data/users.csv",newline="") as file: #evita que queden lineas en blanco
        reader = csv.DictReader(file) #pasa cada línea como si fuera un diccionario
        return list(reader) #devuelve una lista de diccionarios, cada diccionario es un usuario
        
def read_products_json():
    with open("data/products.json") as file:
        return json.load(file) #devuelve una lista de diccionarios, cada diccionario es un producto
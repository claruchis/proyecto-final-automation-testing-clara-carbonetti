# QA Automation - Preentrega - SauceDemo

## Propósito

Automatizar pruebas funcionales sobre SauceDemo utilizando Selenium y Pytest.

Incluye validaciones de:

- Login válido
- Login inválido
- Login vacío
- Inventario
- Carrito de compras

## Tecnologías utilizadas

- Python
- Selenium
- Pytest
- pytest-html

## Instalación

Clonar repositorio:

git clone URL

Instalar dependencias:

pip install -r requirements.txt

## Ejecutar pruebas

pytest -v

## Generar reporte HTML

pytest -v --html=report.html
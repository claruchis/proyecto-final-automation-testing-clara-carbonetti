# Proyecto Final - QA Automation

Proyecto de automatización de pruebas desarrollado como entrega final del curso de QA Automation.

La automatización fue realizada utilizando Selenium WebDriver, Pytest y el patrón de diseño Page Object Model (POM), incorporando además pruebas de API, logging, reportes HTML y captura automática de evidencias.

---

## Tecnologías utilizadas

- Python 3
- Selenium WebDriver
- Pytest
- ChromeDriver
- Requests
- Page Object Model (POM)
- pytest-html
- Logging (`RotatingFileHandler`)
- Git y GitHub

---

## Estructura del proyecto

```
PROYECTO_FINAL/
│
├── data/                  # Datos para pruebas (CSV)
├── logs/                  # Archivos de log
├── page/                  # Page Objects
├── reports/               # Reportes HTML y screenshots
├── tests/                 # Casos de prueba
├── utils/                 # Utilidades (logger, helpers)
│
├── conftest.py            # Fixtures de Pytest
├── pytest.ini             # Configuración de Pytest
├── requirements.txt
└── README.md
```

---

## Funcionalidades automatizadas

### UI Testing

- Login válido
- Login inválido
- Login utilizando datos desde archivo CSV
- Verificación del título de la página
- Validación de productos visibles
- Validación del menú de navegación
- Validación del filtro de productos
- Validación del carrito de compra

### API Testing

- Validación de endpoints utilizando Requests
- Verificación de códigos de estado
- Validación del contenido de las respuestas

---

## Características implementadas

- Page Object Model
- Fixtures reutilizables
- Captura automática de screenshots en fallos
- Reporte HTML de ejecución
- Logger centralizado
- Rotación automática de archivos de log
- Organización modular del proyecto

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/claruchis/proyecto-final-automation-testing-clara-carbonetti.git
```

Ingresar al proyecto:

```bash
cd pre-entrega-automation-testing-clara-carbonetti/PROYECTO_FINAL
```

Crear el entorno virtual:

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución de las pruebas

Ejecutar todos los tests:

```bash
pytest
```

Generar reporte HTML:

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Reporte HTML

El proyecto genera automáticamente un reporte HTML con el resultado de la ejecución de los tests.

![Reporte HTML](docs/report.png)

---

## Evidencias

Durante la ejecución del proyecto se generan automáticamente:

- Reporte HTML
- Capturas de pantalla cuando una prueba falla
- Archivos de log rotativos

---

## Interpretación de los reportes

El proyecto genera un reporte HTML con el resultado de la ejecución de los tests.

En el reporte es posible visualizar:

- Total de pruebas ejecutadas.
- Pruebas aprobadas y fallidas.
- Tiempo de ejecución.
- Detalle de cada caso de prueba.
- Capturas de pantalla asociadas a los tests que fallan.

Además, se generan archivos de log que registran información sobre la ejecución de las pruebas y facilitan el análisis de errores.
---

## Autor

**Clara Carbonetti**

Proyecto desarrollado como práctica de QA Automation utilizando Python, Selenium y Pytest.
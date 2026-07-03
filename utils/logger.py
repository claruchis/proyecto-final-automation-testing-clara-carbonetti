import logging
import pathlib
from datetime import datetime

logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)

#almaceno el timestamp con formato de fecha y hora para que cada log tenga un nombre único
timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S") 

logging.basicConfig(
    filename=logs_dir / f"log_{timestamp}.log",  #defino el nombre del archivo de log
    level=logging.INFO,  #tipo de información que se almacena
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",  #formato del log
    force=True,  #sobreescribe la configuración de logging si ya existe
)

logger =logging.getLogger("Proyecto Final TT")  #obtengo el logger para este módulo

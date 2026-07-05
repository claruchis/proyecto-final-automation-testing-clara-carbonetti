import logging
import pathlib
from logging.handlers import RotatingFileHandler

logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)

log_file = logs_dir / "suite.log"



handler = RotatingFileHandler(
    log_file,  # Archivo de log
    maxBytes=1024 * 1024,  #1 MB
    backupCount=5  # Mantener hasta 5 archivos de log antiguos
)


logging.basicConfig(
    level=logging.INFO,  #tipo de información que se almacena
    handlers=[handler],  #handler que se va a utilizar
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",  #formato del log
    force=True,  #sobreescribe la configuración de logging si ya existe
)

logger = logging.getLogger("Proyecto Final TT")  #obtengo el logger para este módulo



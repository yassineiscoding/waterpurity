
import logging
from pathlib import Path

log_dir = Path("../../logs")
log_dir.mkdir(exist_ok=True)

logger = logging.getLogger("waterpurityLogger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")

file_handler = logging.FileHandler(log_dir / "running_logs.log", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.info("Logger configured successfully.")


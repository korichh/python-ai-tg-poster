import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

log_dir = Path("public")
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / "logs.txt"

formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

file_handler = RotatingFileHandler(
    log_file, maxBytes=1_000_000, backupCount=3, encoding="utf-8"
)
file_handler.setFormatter(formatter)

logger = logging.getLogger("PosterLogger")
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

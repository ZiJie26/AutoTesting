import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from common.load_data_from_file import find_project_root


def setup_logging():
    log_dir = find_project_root() / 'output' / 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_filename = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y%m%d')}.log")

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = TimedRotatingFileHandler(log_filename, when="midnight", backupCount=30, encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

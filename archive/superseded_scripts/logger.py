import logging
import sys

def setup_logger(name="final_thesis", level=logging.INFO):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(name)s: %(message)s', '%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger

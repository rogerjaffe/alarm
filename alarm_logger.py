import logging
from datetime import date
import constants

def log_message(message):
  today = date.today().strftime("%Y-%m-%d")
  date_string = constants.LOGGER_PATH+today+constants.LOGGER_EXT
  a_logger = logging.getLogger()
  a_logger.setLevel(logging.INFO)
  handler = logging.FileHandler(date_string)
  formatter = logging.Formatter(
    fmt='%(asctime)s %(message)s',
    datefmt="%H:%M:%S"
  )
  handler.setFormatter(formatter)
  a_logger.addHandler(handler)
  a_logger.info(message)
  for handler in a_logger.handlers[:]:
    a_logger.removeHandler(handler)


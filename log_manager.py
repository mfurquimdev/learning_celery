import logging
import sys

import parameter

logging_level = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


log = logging.getLogger()
log.setLevel(logging_level.get(parameter.get_env("LOG_LEVEL")))

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging_level.get(parameter.get_env("LOG_LEVEL")))
formatter = logging.Formatter("%(asctime)s - %(levelname)s %(process)d: %(message)s")
ch.setFormatter(formatter)
log.addHandler(ch)

import parameter
import warnings
from typing import List
from typing import Optional
from typing import Tuple

from celery import Celery
from celery.utils.log import get_task_logger
from celery_app.model import Person

app = Celery("messaging")
app.config_from_object("celery_app.celeryconfig")

app.conf.update({"worker_hijack_root_logger": parameter.get_env("GENERATE_LOCAL_LOG")})

logger = get_task_logger(__name__)
warnings.filterwarnings("ignore")


@app.task(name="tasks.say_hello", serializer="pickle")
def say_hello(person: Person) -> Person:
    """
    Prints a hello message by the person.

    Args:
        person (Person): Name, age, and friends of person that sent the message

    Returns:
        (Person)
    """
    logger.info(f"tasks.say_hello({person})")
    logger.info(f"{person.name} is saying hello to {person.friends}")

    return person


@app.task(name="tasks.say_goodbye", serializer="pickle")
def say_goodbye(
    person: Person,
    politely: bool = False,
) -> None:
    """
    Prints a hello message by the person.

    Args:
        person (Person): Name, age, and friends of person that sent the message
        politely (bool): Whether the person will be politely

    Returns:
        None
    """
    logger.info(f"tasks.say_goodbye({person}, {politely})")

    if politely:
        logger.info(f"{person.name}: Farewell my friends {person.friends}")
    else:
        logger.info(f"{person.name}: Run you fools, {person.friends}!")

    return None

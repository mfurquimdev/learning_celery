import parameter
import warnings
from typing import List
from typing import Optional
from typing import Tuple

from celery import Celery
from celery.utils.log import get_task_logger

app = Celery("messaging")
app.config_from_object("celery_app.celeryconfig")

app.conf.update({"worker_hijack_root_logger": parameter.get_env("GENERATE_LOCAL_LOG")})

logger = get_task_logger(__name__)
warnings.filterwarnings("ignore")


@app.task(name="tasks.say_hello", serializer="pickle")
def say_hello(
    name: str,
    age: int,
    friends: List[str] = None,
) -> Tuple[str, int, List[str]]:
    """
    Prints a hello message by the person.

    Args:
        name (str): Name of the person that sent the message
        age (int): Age of the person that sent the message
        friends (List[str]): List of friends of the person that sent the message

    Returns:
        Tuple[str, int, List[str]]: Information about the person
    """
    logger.info(f"tasks.say_hello({name}, {age}, {friends})")
    logger.info(f"{name} is saying hello to {friends}")

    return name, age, friends


@app.task(name="tasks.say_goodbye", serializer="pickle")
def say_goodbye(
    person: Tuple[str, int, List[str]],
    politely: bool = False,
) -> None:
    """
    Prints a hello message by the person.

    Args:
        name (str): Name of the person that sent the message
        age (int): Age of the person that sent the message
        friends (List[str]): List of friends of the person that sent the message

    Returns:
        Tuple[str, int, List[str]]: Information about the person
    """
    (name, age, friends) = person
    logger.info(f"tasks.say_goodbye({name}, {age}, {friends}, {politely})")

    if politely:
        logger.info(f"{name}: Farewell my friends {friends}")
    else:
        logger.info(f"{name}: Run you fools, {friends}!")

    return None

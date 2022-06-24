from typing import List
from typing import Optional

from log_manager import log
from celery import chain

from celery_app.tasks import say_hello
from celery_app.tasks import say_goodbye
from celery_app.model import Person


def build_interaction(name: str, age: int, friends: List[str] = None, politely=False):

    person = Person(
        name=name,
        age=age,
        friends=friends,
    )

    VIP = ["Mateus"]

    if name in VIP:
        log.info(f"{name} is VIP")
        politely = True

    tasks = [
        say_hello.si(person).set(queue="interaction_queue"),
        say_goodbye.s(
            politely=politely,
        ).set(queue="interaction_queue"),
    ]

    return chain(*tasks)

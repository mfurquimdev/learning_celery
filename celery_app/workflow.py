from typing import List
from typing import Optional

from celery import chain

from celery_app.tasks import say_hello
from celery_app.tasks import say_goodbye


def build_interaction(name: str, age: int, friends: List[str] = None, politely=False):
    VIP = ["Mateus"]

    if name in VIP:
        politely = True

    tasks = [
        say_hello.si(
            name,
            age,
            friends,
        ).set(queue="interaction_queue"),
        say_goodbye.s(
            politely=politely,
        ).set(queue="interaction_queue"),
    ]

    return chain(*tasks)

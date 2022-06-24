import pandas as pd
from typing import List
from log_manager import log
from celery_app.workflow import build_interaction


def send_message(name: str, age: int, friends: List[str] = None):
    """
    Sends message to rabbitmq

    Args:
        name (str): Name of the person that sent the message
        age (int): Age of the person that sent the message
        friends (List[str]): List of friends of the person that sent the message

    Returns:
        task_id: ID of created message
    """
    workflow_interaction = build_interaction(name, age, friends, politely=True)

    return workflow_interaction.apply_async()

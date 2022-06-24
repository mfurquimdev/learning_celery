from typing import Dict

from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.messaging.controller import send_message
from app.messaging.model import MessagingInput
from log_manager import log

router = APIRouter()


@router.post(
    "/messaging",
    summary="Create a message on the rabbitmq",
    response_description="ID of created message",
    response_model=Dict,
)
def send_messaging(input: MessagingInput):
    log.info(f"POST /messaging with data {input}")

    task = send_message(input.name, input.age, input.friends)
    result = {"task_id": task.id}

    return JSONResponse(result)

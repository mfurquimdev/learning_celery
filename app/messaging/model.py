from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class MessagingInput(BaseModel):
    name: str = Field(
        title="Person's name",
        descrition="Name of the person that sent the message",
    )

    age: int = Field(
        title="Person's age",
        descrition="Age of the person that sent the message",
    )

    friends: Optional[List[str]] = Field(
        default=None,
        title="Person's friends",
        descrition="List of friends of the person that sent the message",
    )

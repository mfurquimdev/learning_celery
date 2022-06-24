from dataclasses import dataclass, field
from typing import List


@dataclass(repr=True)
class Person:
    name: str
    age: int
    friends: List[str] = field(default_factory=list)

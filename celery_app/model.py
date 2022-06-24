from dataclasses import dataclass, field
from typing import List
import pandas as pd


@dataclass(repr=True)
class Person:
    name: str
    age: int
    friends: List[str] = field(default_factory=list)
    df: pd.DataFrame = field(default_factory=pd.DataFrame())

from dataclasses import dataclass
from typing import Optional


@dataclass
class Room:
    id: Optional[int]
    name: str
    available: bool
    description: str
    location_price: int

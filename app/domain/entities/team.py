from dataclasses import dataclass
from typing import List

from app.domain.entities.player import Player


@dataclass
class Team:
    name: str
    players: List[Player]

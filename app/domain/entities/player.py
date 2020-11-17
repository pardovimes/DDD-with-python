from dataclasses import dataclass
from datetime import date

from app.domain.value_objects.dorsal import Dorsal


@dataclass
class Player:
    name: str
    position: str
    dorsal: Dorsal
    nationality: str
    birth_date: date
    contract_until: date

from dataclasses import dataclass
from app.domain.exceptions import InvalidDorsalNumber


@dataclass
class Dorsal:
    number: int

    def __post_init__(self):
        if self.number < 0:
            raise InvalidDorsalNumber("Dorsal number is little than 0")
from dataclasses import dataclass

from app.domain.value_objects.dorsal import Dorsal


@dataclass
class GetPlayerRequest:
    dorsal: Dorsal

from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.player import Player
from app.domain.value_objects.dorsal import Dorsal


class PlayerRepository(ABC):
    @abstractmethod
    def get_by_dorsal(self, dorsal: Dorsal) -> Optional[Player]:
        """ Returns a player given a dorsal.
        If no player is found, returns None. """

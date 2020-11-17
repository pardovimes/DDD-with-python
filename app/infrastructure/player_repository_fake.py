from datetime import date
from typing import Optional

from app.domain.entities.player import Player
from app.domain.repositories.player_repository import PlayerRepository
from app.domain.value_objects.dorsal import Dorsal


class PlayerRepositoryFake(PlayerRepository):

    PLAYERS = [
        Player(
            name="Toni",
            position="Portero",
            dorsal=Dorsal(5),
            nationality="Español",
            birth_date=date.today(),
            contract_until=date.today(),
        )
    ]

    def get_by_dorsal(self, dorsal: Dorsal) -> Optional[Player]:
        for player in self.PLAYERS:
            if player.dorsal == dorsal:
                return player
        return None

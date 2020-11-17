from dataclasses import dataclass

from app.domain.entities.player import Player


@dataclass
class GetPlayerResponse:
    player: Player

from app.application.exceptions import PlayerNotFound
from app.application.get_player_request import GetPlayerRequest
from app.application.get_player_response import GetPlayerResponse
from app.domain.entities.player import Player
from app.domain.repositories.player_repository import PlayerRepository


class GetPlayer:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def execute(self, get_player_request: GetPlayerRequest) -> GetPlayerResponse:

        player = self.player_repository.get_by_dorsal(get_player_request.dorsal)

        if player is None:
            raise PlayerNotFound("hola")

        return GetPlayerResponse(player=player)

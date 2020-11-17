from app.application.get_player import GetPlayer
from app.infrastructure.player_repository_fake import PlayerRepositoryFake


def get_get_player():
    return GetPlayer(player_repository=PlayerRepositoryFake())

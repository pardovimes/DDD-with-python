import json

from app.application.exceptions import PlayerNotFound
from app.application.get_player_request import GetPlayerRequest
from app.di.use_cases import get_get_player
from app.domain.value_objects.dorsal import Dorsal
from app.infrastructure.serializers.player_serializer import PlayerSerializer
from flask import Blueprint, Response

blueprint = Blueprint("views", __name__)


@blueprint.route("/players/<int:dorsal_number>", methods=["GET"])
def player(dorsal_number):
    get_player = get_get_player()
    get_player_request = GetPlayerRequest(Dorsal(dorsal_number))

    try:
        player_response = get_player.execute(get_player_request)
    except PlayerNotFound as e:
        return Response(response=json.dumps({"msg": str(e)}), status=404, content_type="application/json")

    player_serializer = PlayerSerializer()

    return Response(
        response=json.dumps(player_serializer.dump(player_response.player)), status=200, content_type="application/json"
    )

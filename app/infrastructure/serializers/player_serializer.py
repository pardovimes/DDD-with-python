from app.infrastructure.serializers.dorsal_serializer import DorsalSerializer
from marshmallow import Schema, fields


class PlayerSerializer(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()
    name = fields.Str()
    position = fields.Str()
    dorsal = fields.Nested(DorsalSerializer)
    nationality = fields.Str()
    birth_date = fields.Date()
    contract_until = fields.Date()

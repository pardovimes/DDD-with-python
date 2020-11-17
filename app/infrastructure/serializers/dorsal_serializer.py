from marshmallow import Schema, fields


class DorsalSerializer(Schema):
    number = fields.Int()

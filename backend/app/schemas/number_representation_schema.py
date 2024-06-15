from marshmallow import Schema, fields, post_load

from backend.app.schemas.ieee_format_schema import IEEEFormatSchema
from backend.app.schemas.binary_number_schema import BinaryNumberSchema
from backend.app.schemas.denary_number_schema import DecimalNumberSchema, FractionalNumberSchema
from backend.app.schemas.ieee_float_schema import IEEEFloatSchema


class NumberRepresentationSchema(Schema):
    ieee_format = fields.Nested(IEEEFormatSchema, required=False)
    binary_number = fields.Nested(BinaryNumberSchema, required=False)
    decimal_number = fields.Nested(DecimalNumberSchema, required=False)
    fractional_number = fields.Nested(FractionalNumberSchema, required=False)
    ieee_float = fields.Nested(IEEEFloatSchema, required=False)

    @post_load
    def make_number_representation(self, data):
        from backend.app.models.number_representation import NumberRepresentation
        return NumberRepresentation(**data)

    def serialize(self, data):
        return self.dump(data)

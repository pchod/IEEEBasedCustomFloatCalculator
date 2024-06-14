# denary_number_schema.py

from marshmallow import Schema, fields, post_load, ValidationError, validates_schema

from backend.app.models.denary_number import FractionalNumber, DecimalNumber


class FractionalNumberSchema(Schema):
    numerator = fields.Integer(required=True)
    denominator = fields.Integer(required=True)
    is_positive = fields.Boolean(required=True)
    numerator_entered = fields.Integer(dump_only=True)
    denominator_entered = fields.Integer(dump_only=True)
    den_is_power_of_2 = fields.Boolean(dump_only=True)
    decimal_float_derived = fields.Float(dump_only=True)

    @validates_schema
    def validate_schema(self, data, **kwargs):
        numerator = data.get("numerator")
        numerator_entered = data.get("numerator_entered")
        denominator = data.get("denominator")
        denominator_entered = data.get("denominator_entered")
        decimal_float_derived = data.get("decimal_float_derived")

        if (numerator or numerator_entered) < 0:
            raise ValidationError("Numerator cannot be negative value.")

        if (denominator or denominator_entered) < 0:
            raise ValidationError("Denominator cannot be negative value.")

        if (denominator or denominator_entered) == 0:
            raise ValidationError("Denominator cannot be zero value.")

        if decimal_float_derived < 0:
            raise ValidationError("Decimal float cannot be negative value.")

    @post_load
    def create_fractional_number(self, data):
        return FractionalNumber(**data)

    def serialize(self, fractional_number):
        return self.dump(fractional_number)


class DecimalNumberSchema(Schema):
    int_part = fields.String(required=True)
    fractional_part = fields.String(required=True)
    is_positive = fields.Boolean(required=True)
    decimal_number = fields.String(dump_only=True)
    is_decimal_zero = fields.Boolean(dump_only=True)
    numerator_derived = fields.Integer(dump_only=True)
    denominator_derived = fields.Integer(dump_only=True)
    den_derived_is_power_of_2 = fields.Boolean(dump_only=True)

    @post_load
    def create_decimal_number(self, data):
        return DecimalNumber(**data)

    def serialize(self, decimal_number):
        return self.dump(decimal_number)
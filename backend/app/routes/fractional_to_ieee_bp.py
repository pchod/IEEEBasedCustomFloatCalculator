from flask import Blueprint, request, jsonify, make_response
from marshmallow import ValidationError

from backend.app.schemas import denary_number_schema, ieee_format_schema, number_representation_schema
from backend.app.services.calculator_service import CalculatorService

fractional_to_ieee_bp = Blueprint('fractional_to_ieee_bp', __name__)
fraction_schema = denary_number_schema.FractionalNumberSchema()
number_representation_schema = number_representation_schema.NumberRepresentationSchema()


@fractional_to_ieee_bp.route('/api/v1/fractional_to_ieee/<string:ieee_format>', methods=['POST'])
def fractional_to_ieee(ieee_format):
    if request.content_type != 'application/json':
        return make_response(jsonify({"error": "Invalid content type, must be application/json"}), 400)

    try:
        data = request.get_json()
        if not data:
            return make_response(jsonify({"error": "No data provided"}), 400)

        # Load and validate fractional number data
        fractional_number = fraction_schema.load(data.get('fractional_number'))

        # Determine the IEEE format schema based on the URL parameter
        if ieee_format == "16bit":
            ieee_format_instance = ieee_format_schema.IEEE16BitFormatSchema().load({})
        elif ieee_format == "32bit":
            ieee_format_instance = ieee_format_schema.IEEE32BitFormatSchema().load({})
        elif ieee_format == "64bit":
            ieee_format_instance = ieee_format_schema.IEEE64BitFormatSchema().load({})
        elif ieee_format == "custom":
            ieee_format_instance = ieee_format_schema.IEEECustomLengthFormatSchema().load(data.get('ieee_format'))
        else:
            raise ValidationError(f"Unsupported format {ieee_format}")

        # Calculate the IEEE representation
        number_representation_instance = CalculatorService.calculate_ieee_from_fractional(fractional_number, ieee_format_instance)
        print(f"Final number representation instance: {number_representation_instance}")

        # Serialize the result
        result = number_representation_schema.dump(number_representation_instance)
        print(f"Serialized result: {result}")
        return jsonify(result)

    except ValidationError as err:
        return make_response(jsonify({"error": err.messages}), 400)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

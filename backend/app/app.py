from flask import Flask
from backend.app.routes.fractional_to_ieee_bp import fractional_to_ieee_bp
from backend.app.routes.decimal_point_to_ieee_bp import decimal_point_to_ieee_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(fractional_to_ieee_bp)
    app.register_blueprint(decimal_point_to_ieee_bp)
    return app

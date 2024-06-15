from flask import Flask
from backend.app.routes.fractional_to_ieee_bp import fractional_to_ieee_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(fractional_to_ieee_bp)
    return app

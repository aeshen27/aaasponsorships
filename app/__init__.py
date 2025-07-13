from flask import Flask
from .companies.routes import companies

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)
    app.register_blueprint(companies)

    return app
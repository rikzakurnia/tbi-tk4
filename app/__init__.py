import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    # Import and register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app

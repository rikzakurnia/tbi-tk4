import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Setup env
    app.config['FLASK_APP'] = os.getenv('FLASK_APP')
    app.config['ENV_EXAMPLE'] = os.getenv('ENV_EXAMPLE')

    # Import and register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app

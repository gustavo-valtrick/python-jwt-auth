from flask import Flask
from src.models.settings.db_connection_handler import db_connection_handler
from src.main.routes import ACTIVE_BLUEPRINTS

db_connection_handler.connect()

app = Flask(import_name=__name__)

for bp in ACTIVE_BLUEPRINTS:
    app.register_blueprint(blueprint=bp)

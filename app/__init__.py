from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.setup import setup_app
setup_app(app)

from app import views

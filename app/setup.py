from app import data
import threading


def setup_app(app):
    data.update_recomendations()
    threading.Timer(
        app.config['UPDATE_DELAY'],
        data.update_recomendations
    ).start()

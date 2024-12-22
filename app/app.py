from flask import Flask
from .config import Config
from routes.generales import define_routes  # Import de la fonction pour définir les routes ; solution ChatGPT parce que le terminal m'affichait toujours l'erreur ModuleNotFoundError: No module named 'routes.app'

app = Flask(__name__,template_folder="../templates")
app.config.from_object(Config)

define_routes(app)
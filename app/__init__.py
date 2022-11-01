from flask import Flask
from senha import senha_bp
from blueprint1 import blueprint1
from blueprint2 import blueprint2

app = Flask(__name__)
app.config.from_object('app.config.Configuracao')
app.register_blueprint(senha_bp, url_prefix = '/senha')
app.register_blueprint(blueprint1, url_prefix='/blueprint1')
app.register_blueprint(blueprint2, url_prefix='/blueprint2')

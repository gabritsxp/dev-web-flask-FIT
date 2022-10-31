from flask import Flask
from senha import senha_bp
from blueprint1 import formulario_bp
from blueprint2 import sobre_bp

app = Flask(__name__)
app.config.from_object('app.config.Configuracao')

app.register_blueprint(senha_bp, url_prefix='/senha')
app.register_blueprint(formulario_bp, url_prefix='/blueprint1')
app.register_blueprint(sobre_bp, url_prefix='/blueprint2')

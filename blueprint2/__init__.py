from flask import Blueprint

sobre_bp = Blueprint(
    'sobre',
    __name__,
    template_folder='templates'
)

from . import controles

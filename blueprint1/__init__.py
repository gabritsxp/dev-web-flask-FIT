from flask import Blueprint

formulario_bp = Blueprint(
    'formulario',
    __name__,
    template_folder='templates'
)

from . import controles

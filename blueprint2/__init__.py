from flask import Blueprint

blueprint2 = Blueprint(
    'blueprint2',
    __name__,
    template_folder='templates'
)

from . import controles

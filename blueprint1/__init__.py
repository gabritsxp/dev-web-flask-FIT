from flask import Blueprint

blueprint1 = Blueprint(
    'blueprint1',
    __name__,
    template_folder='templates'
)

from . import controles

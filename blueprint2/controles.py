from flask import render_template
from blueprint2 import sobre_bp


@sobre_bp.route('/')
def get_sobre():
    print('chamou o get')
    return render_template('sobre_o_curso.html')



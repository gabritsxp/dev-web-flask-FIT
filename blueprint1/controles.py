from blueprint1 import formulario_bp
from flask import render_template, session, request


@formulario_bp.route('/')
def get_contato():
    print('chamou o get')

    return render_template('formulario.html')


@formulario_bp.route('/', methods=['POST'])
def post_form():
    print('chamou o post')
    print(request.form)
    comunicado = f'Olá {request.form["nome"]}, recebemos sua mensagem e em breve alguém da nossa equipe entrará em contato'

    return render_template('formulario.html', comunicado=comunicado)


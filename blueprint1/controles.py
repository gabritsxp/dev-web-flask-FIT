from blueprint1 import blueprint1
from flask import render_template, session, request


@blueprint1.route('/')
def get_contato():
    print('chamou o get')

    return render_template('blueprint1.html')


@blueprint1.route('/', methods=['POST'])
def post_form():
    print('chamou o post')
    print(request.form)
    comunicado = f'Olá {request.form["nome"]}, recebemos sua mensagem e em breve alguém da nossa equipe entrará em contato'

    return render_template('blueprint1.html', comunicado=comunicado)


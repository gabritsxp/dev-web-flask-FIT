from flask import render_template
from blueprint2 import blueprint2


@blueprint2.route('/')
def get_sobre():
    print('chamou o get')
    return render_template('blueprint2.html')



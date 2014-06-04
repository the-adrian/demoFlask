import flask, flask.views
from flask import request

class Login(flask.views.MethodView):
    def post(self):
        usuario = None
        error = None
        if request.method == 'POST':
            usuario = request.form['usuario']
        else:
            error = 'basura'
        return flask.render_template('login.html', usuario=usuario, error=error)

    def get(self):
        usuario = None
        error = None
        if request.method == 'POST':
            usuario = request.form['usuario']
        else:
            error = 'basura'
        return flask.render_template('login.html', usuario=usuario, error=error)
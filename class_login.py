import flask, flask.views
from flask import request

class Login(flask.views.MethodView):
    def post(self):
        usuario = None
        password =None
        message = None
        if request.method == 'POST':
            usuario = request.form['usuario']
            password = request.form['password']
            if usuario == 'Adrian' and password == '123':
                message = 'Welcome'
                return flask.render_template('login.html', message = message)
            else:
                message = 'Access denied'
                return flask.render_template('login.html',message = message)


    def get(self):
        usuario = None
        error = None
        if request.method == 'POST':
            usuario = request.form['usuario']
        else:
            error = 'basura'
        return flask.render_template('login.html', usuario=usuario, error=error)
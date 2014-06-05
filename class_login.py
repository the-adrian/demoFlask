import flask, flask.views
from flask import request
from flaskext.mysql import MySQL


class Login(flask.views.MethodView):
    def post(self):
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
       return flask.render_template('login.html')

import flask, flask.views
from flask import request

class Login(flask.views.MethodView):
    def post(self):
        message = None
        if request.method == 'POST':
            usuario = request.form['usuario']
            password = request.form['password']
            if usuario == 'Adrian' and password == '123':
                message = 'Welcome'

                return flask.render_template('servicios.html', message = usuario)
            else:
                message = 'Access denied'
                #flash('probando flash')
                return flask.render_template('login.html', message = message)


    def get(self):
       return flask.render_template('login.html')

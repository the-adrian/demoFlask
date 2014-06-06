import flask, flask.views
from flask import request, flash
from flaskext.mysql import MySQL
import flask
import class_db

mysql = MySQL()
app = flask.Flask(__name__)

class Login(flask.views.MethodView):

    def post(self):

        message = None
        if request.method == 'POST':
            usuario = request.form['usuario']
            password = request.form['password']
            query = "SELECT * FROM USUARIOS WHERE Nombre ='" + usuario + "' AND Password = '" + password + "'"
            data = class_db.database(query)

            if data is None:
                message = 'Access denied'
                return flask.render_template('login.html', message = message)
            else:
                message = 'Welcome'
                return flask.render_template('servicios.html', message = usuario)


    def get(self):
       return flask.render_template('login.html')
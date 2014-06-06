import flask, flask.views
from flask import request, flash
from flaskext.mysql import MySQL
from class_services import Services
import flask
import class_db
import class_services

mysql = MySQL()
app = flask.Flask(__name__)

class Login(flask.views.MethodView):
    def post(self):
        message = None
        if request.method == 'POST':
            usuario = request.form['usuario']
            password = request.form['password']
            query = "SELECT * FROM jc_identificaciones where usuario_identificacion  = '"+usuario+"'"
            data = class_db.database(query)

            if data is None:
                return flask.redirect(flask.url_for('login'))
            else:
                return flask.redirect(flask.url_for('services'))


    def get(self):
       return flask.render_template('login.html', message = 'Access denied')
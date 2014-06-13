import flask, flask.views
from flask import request, flash, session
from flaskext.mysql import MySQL

import flask
import class_db
import class_home
import os

mysql = MySQL()
app = flask.Flask(__name__)

class Login(flask.views.MethodView):
    def post(self):
        message = None
        if request.method == 'POST':
            usuario = request.form['usuario']
            password = request.form['password']
            query = "SELECT * FROM USUARIOS where Nombre  = '"+usuario+"' AND Password = '" + password +"'"
            data = class_db.validar_usuario(query)
            if data is None:
                flash('Usuario o Password Incorrectos')
                return flask.redirect(flask.url_for('login'))
            else:
                #session['logged_in'] = True
                session['username'] = usuario
                return flask.redirect(flask.url_for('home'))



    def get(self):
       return flask.render_template('login.html', message = 'Access denied')

    def logout(self):
        session.pop('username',None)
        return flask.redirect(flask.url_for('login'))
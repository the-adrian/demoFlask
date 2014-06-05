import flask
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import os
import sqlite3

#----------- Configuracion de la base de datos ---------
app.config.update(dic(
    DATABASE = os.path.join(app.route_path, 'usuaios.db'),
    DEBUG = True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = '123'
))

#------------vistas
from class_login import Login
from class_services import Services
#fin-----------------------

app = flask.Flask(__name__)
#########inicializacion del servidor####################
__SERVER__ = 'localhost'
app.debug = True
#fin de los parametros para la inicializacion del serviro

@app.route('/')
def infoServer():
  return render_template('login.html')

#rutas para visualizacion del templantes
app.add_url_rule('/login/', view_func=Login.as_view('login') , methods=['POST','GET'])
app.add_url_rule('/services/', view_func=Services.as_view('services'))

##########Inicializacion del servidor ##############################
if __name__ == '__main__':
    app.run(host=__SERVER__)
########################################


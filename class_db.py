#-*- coding_ utf-8 -*-
__author__ = 'adrian'
from flask import request, flash
from flaskext.mysql import MySQL
import flask
import logger


mysql = MySQL()
try:
    app = flask.Flask(__name__)
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'USERS'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)
    cursor = mysql.connect().cursor()
except:
    log = logger
    log.log('ERROR','DATABASE','ERROR','NO SE PUEDE CONECTAR CON LA BASE DE DATOS')

def validar_usuario(query):
    if query.upper().startswith('SELECT'):
        cursor.execute(query)
        data = cursor.fetchone()
        return data

def consultar_usuarios(query):
    cursor.execute(query)
    data = cursor.fetchall()
    return data




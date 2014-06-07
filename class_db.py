#-*- coding_ utf-8 -*-
__author__ = 'adrian'
from flask import request, flash
from flaskext.mysql import MySQL
import flask

mysql = MySQL()

app = flask.Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'USERS'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


def validar_usuario(query):
    cursor = mysql.connect().cursor()
    if query.upper().startswith('SELECT'):
        cursor.execute(query)
        data = cursor.fetchone()
        return data

def consultar_usuarios(query):
    cursor = mysql.connect().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data




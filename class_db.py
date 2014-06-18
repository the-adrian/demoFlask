#-*- coding_ utf-8 -*-
from plistlib import _dateFromString

__author__ = 'adrian'
import libgral
from flaskext.mysql import MySQL
import flask
import logger


mysql = MySQL()
try:
    app = flask.Flask(__name__)
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'Proyecto'
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

def consultar_ventas(dateStart, dateEnd):
    dateStart = libgral.separateDate(dateStart)
    dateEnd = libgral.separateDate(dateEnd)
    # 2014/06/13 11:46:25
    # 2014/06/13 14:05:37
    query = "SELECT No_Serie, Turno, Fecha, Hora, Ticket, Tarifa, Total FROM Tabla_Ventas " \
            "WHERE Fecha BETWEEN STR_TO_DATE('"+dateStart[0]+"', '%Y/%m/%d') AND STR_TO_DATE('"+dateEnd[0]+"','%Y/%m/%d')" \
            "AND Hora BETWEEN TIME_FORMAT('"+dateStart[1]+"','%T') AND TIME_FORMAT('"+dateEnd[1]+"','%T');"

    cursor.execute(query)
    data = cursor.fetchone()
    return data






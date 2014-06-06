#-*- coding_ utf-8 -*-
__author__ = 'adrian'
from flaskext.mysql import MySQL
#-----configuracion de la base de datos----------------------
mysql = MySQL()
app = flask.Flask(__name__)
def db(query):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = ''
    app.config['MYSQL_DATABASE_DB'] = 'bd_groupware'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)
    cursor = mysql.get_db().cursor()
    if query.upper().startswith('SELECT'):
        cursor.execute(query)
        data = cursor.fetchone()
        return data
    else:
        pass



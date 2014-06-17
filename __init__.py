import flask
from flask import render_template , session
#------------vistas
from class_login import Login
from class_home import Home
import os
from class_reportes import Reportes
app = flask.Flask(__name__)
#########inicializacion del servidor####################
__SERVER__ = 'localhost'
app.debug = True
#fin de los parametros para la inicializacion del serviro
app.secret_key = os.urandom(24)
@app.route('/')
def infoServer():
    return render_template('login.html')

@app.route('/logout')
def logout():
    del session['username']
    return flask.redirect(flask.url_for('login'))

#rutas para visualizacion del templantes
app.add_url_rule('/login/', view_func=Login.as_view('login') , methods=['POST','GET'])
app.add_url_rule('/home/', view_func=Home.as_view('home') , methods=['POST','GET'])
app.add_url_rule('/reportes/', view_func=Reportes.as_view('reportes'), methods=['POST', 'GET'])
##########Inicializacion del servidor ##############################
if __name__ == '__main__':
    app.run(host=__SERVER__)
########################################


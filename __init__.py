import flask

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
  return 'Servidor Mageia con Flask Inicalizando...... <a href=\'/login/\'>login</a> <a href=\'/services/\'>Servicios</a>'

#rutas para visualizacion del templantes
app.add_url_rule('/login/', view_func=Login.as_view('login') , methods=['POST','GET'])
app.add_url_rule('/services/', view_func=Services.as_view('services'))

##########Inicializacion del servidor ##############################
if __name__ == '__main__':
    app.run(host=__SERVER__)
########################################


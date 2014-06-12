import flask, flask.views
import class_db
from class_lights import Ligths
from flask import request

class Services(flask.views.MethodView):
    def get(self):
        #objLights = Ligths()
        #objLights.control()
        return flask.render_template('servicios.html')

    def conultaVentas(self):
       pass

    def post(self):
         if request.method == 'POST':
            fechaInicio = request.form['fechaInicio']
            fechaFin = request.form['fechaFin']
            print fechaInicio


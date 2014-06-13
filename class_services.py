import flask, flask.views
import class_db
from class_lights import Ligths
from flask import request, session

class Services(flask.views.MethodView):
    def get(self):
        #objLights = Ligths()
        #objLights.control()
        logged_in = session['logged_in']
        if logged_in:
            return flask.redirect(flask.url_for('services'))
        else:
            return flask.redirect(flask.url_for('login'))

    def conultaVentas(self):
       pass

    def post(self):
         if request.method == 'POST':
            fechaInicio = request.form['fechaInicio']
            fechaFin = request.form['fechaFin']
            print fechaInicio


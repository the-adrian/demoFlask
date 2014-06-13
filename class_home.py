#-*- coding: utf-8 -*-
__author__ = 'aramirez'
import flask, flask.views
import class_db
from class_lights import Ligths
from flask import request, session , render_template

class Home(flask.views.MethodView):
    def get(self):
        #objLights = Ligths()
        #objLights.control()
        if session:
            return render_template('principal.html', nomUsuario=session['username'])
        else:
            return flask.redirect(flask.url_for('login'))

    def conultaVentas(self):
       pass

    def post(self):
         if request.method == 'POST':
            fechaInicio = request.form['fechaInicio']
            fechaFin = request.form['fechaFin']
            print fechaInicio

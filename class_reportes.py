#-*- coding: utf-8 -*-
from flask import render_template, redirect,request
import flask
from web.contrib.template import render_cheetah
import class_db

class Reportes(flask.views.MethodView):
    def post(self):
        fechaInicio = request.form['fechaInicio']
        fechaFin = request.form['fechaFin']
        tabla_ventas = class_db.consultar_ventas(fechaInicio, fechaFin)
        if tabla_ventas == None:
            msg = True
            return render_template('home.html', msg = msg)
        else:
            return render_template('home.html',tabla_ventas = tabla_ventas, fechaFin = fechaFin, fechaInicio = fechaInicio)
    def get(self):
        return render_template('home.html')


#-*- coding: utf-8 -*-
from flask import render_template, redirect,request
import flask
import class_db

class Reportes(flask.views.MethodView):
    def post(self):
        fechaInicio = request.form['fechaInicio']
        fechaFin = request.form['fechaFin']
        tabla_ventas = class_db.consultar_ventas(fechaInicio, fechaFin)
        return render_template('reportes.html', tabla_ventas = tabla_ventas)

    def get(self):
        return render_template('reportes.html')


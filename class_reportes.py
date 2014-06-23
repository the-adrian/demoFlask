#-*- coding: utf-8 -*-
from flask import render_template, redirect,request
import flask
import class_db

num_col = 7
class Reportes(flask.views.MethodView):
    def post(self):
        fechaInicio = request.form['fechaInicio']
        fechaFin = request.form['fechaFin']
        tabla_ventas = class_db.consultar_ventas(fechaInicio, fechaFin)
        codigo_tabla = ""
        if tabla_ventas == None:
            msg = True
            return render_template('home.html', msg = msg)
        else:
            for venta in tabla_ventas:
                codigo_tabla += str('<tr class="active">')
                for indice in range(num_col):
                    codigo_tabla += str("<td>")+ str(tabla_ventas[indice + 1]) + str("</td>")

                str("</tr>")
            return render_template('home.html',codigo_tabla = codigo_tabla, fechaFin = fechaFin, fechaInicio = fechaInicio)
    def get(self):
        return render_template('home.html')


##### Notas
"""
para ver el numero de serie

  <!--{% set Num_Serie = tabla_ventas[0] %}<p>Número de Serie: <strong> {{ Num_Serie[12:] }} </strong></p>-->
"""


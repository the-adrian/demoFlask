import flask, flask.views
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

class Login(flask.views.MethodView):
    def post(self):
        usuario = None
        password =None
        message = None
        if request.method == 'POST':
            usuario = request.form['usuario']
            password = request.form['password']
            if usuario == 'Adrian' and password == '123':
                message = 'Welcome'

                return flask.render_template('servicios.html', message = usuario)
            else:
                message = 'Access denied'
                #flash('probando flash')
                return flask.render_template('login.html', message = message)


    def get(self):
        usuario = None
        error = None
        if request.method == 'POST':
            usuario = request.form['usuario']
        else:
            error = 'basura'
        return flask.render_template('login.html', usuario=usuario, error=error)
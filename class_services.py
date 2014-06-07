import flask, flask.views
import class_db
from class_lights import Ligths

class Services(flask.views.MethodView):
    def get(self):
        objLights = Ligths()
        objLights.control()
        return flask.render_template('servicios.html', usuarios = self.dameUsuarios())

    def dameUsuarios(self):
        tabla = class_db.consultar_usuarios("SELECT ID, Nombre from USUARIOS")
        return  tabla

    def post(self):
        result = eval(flask.request.form['expresion'])
        flask.flash(result)
        return  flask.redirect(flask.url_for('servicios'))


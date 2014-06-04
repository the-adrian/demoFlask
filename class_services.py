import flask, flask.views

class Services(flask.views.MethodView):
    def get(self):
        return flask.render_template('servicios.html')
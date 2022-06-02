import flask
from flask import Flask

from forms import *

# app = Flask(__name__)
app = Flask(__name__, static_folder="../static", template_folder="../templates")
app.config['SECRET_KEY'] = "blabla"


@app.route('/')
def index():
    return app.send_static_file("html/index.html")


@app.route('/templates')
def templating_index():
    return flask.render_template("index_templating.html", username="Gruzin")
    # return flask.render_template("index_loop_templating.html", username="Gruzin", active_users=['Rafist0', "Karkulak", "Michalwrpo", "Owca"])
    # return flask.render_template("index_loop_templating.html", username=flask.request.args['email'], active_users=['Rafist0', "Karkulak", "Michalwrpo", "Owca"])


@app.route("/input")
def input_form_test():
    form = CustomUsernameForm()
    return flask.render_template("input_form.html", form=form)


@app.route('/hw')
def hello_world():
    return {"message": 'Hello World'}


@app.route("/redirect")
def redirect_route():
    return flask.redirect(flask.url_for("templating_index"))


@app.errorhandler(404)
def handler404(error):
    return app.send_static_file("html/404.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1")
    # app.run(host="0.0.0.0")
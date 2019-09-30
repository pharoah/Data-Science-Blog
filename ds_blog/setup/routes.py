from flask import Blueprint, render_template, request

setup = Blueprint('setup', __name__)

@setup.route("/setup")
def setup_installation():
    return render_template('setup.html', title='Setup')

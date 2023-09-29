from flask import Blueprint
from flask import render_template



bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')

@bp_usuarios.route('/create')
def create():
    return render_template('usuarios_create.html')



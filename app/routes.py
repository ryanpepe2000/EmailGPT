from flask import render_template, Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html', title="Home")

@bp.route('/about')
def about():
    return render_template('about.html', title="About")
from flask import render_template, Blueprint
core = Blueprint('core', __name__)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/contact')
#TODO add get and post
def contact():
    return render_template('contact.html')

@core.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
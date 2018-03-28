from flask import render_template
from . import home

@home.app_errorhandler(404)
def page_not_found(e):
    return render_template('home/404.html'), 404

@home.app_errorhandler(500)
def internal_server_error(e):
    return render_template('home/500.html'), 500
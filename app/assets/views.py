from . import assets
from flask import render_template

@assets.route('/assets/hosts/')
def hosts():
    return render_template('assets/host_list.html')
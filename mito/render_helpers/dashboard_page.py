from flask import render_template

from mito import app


def render_dat():
    with app.app_context():
        return render_template('dashboard_page/notes.html')


def render_layout():
    with app.app_context():
        return render_template('dashboard_page/layout.html')

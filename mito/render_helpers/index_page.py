from flask import render_template

from mito import app


def render_main_content():
    with app.app_context():
        return render_template('index_page/main_content.html')


def render_layout():
    with app.app_context():
        return render_template('index_page/layout.html')

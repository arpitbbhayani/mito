from flask import render_template

from mito import app


def render_pre_body():
    with app.app_context():
        return render_template('common/pre_body.html')


def render_post_body():
    with app.app_context():
        return render_template('common/post_body.html')


def render_top_menu(is_authenticated):
    with app.app_context():
        return render_template('menus/top_menu.html', is_authenticated=is_authenticated)

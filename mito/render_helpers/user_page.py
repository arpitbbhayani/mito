from flask import render_template

from mito import app
from mito.services import user_service


def render_user_action_buttons():
    with app.app_context():
        return render_template('user_page/user_actions.html')


def render_user_profile(user_id):
    with app.app_context():
        user, error = user_service.get_by_id(user_id)
        if error:
            return error.description

        return render_template('user_page/user_profile.html', user=user)


def render_layout():
    with app.app_context():
        return render_template('user_page/layout.html')

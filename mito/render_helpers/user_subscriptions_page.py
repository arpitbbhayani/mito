from flask import render_template

from mito import app


def render_user_subscriptions_action_buttons():
    with app.app_context():
        return render_template('user_subscriptions_page/user_subscriptions_actions.html')


def render_user_subscription(user_subscription):
    with app.app_context():
        return render_template('user_subscriptions_page/user_subscriptions.html', user_subscription=user_subscription)


def render_layout():
    with app.app_context():
        return render_template('user_subscriptions_page/layout.html')

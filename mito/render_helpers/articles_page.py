from flask import render_template

from mito import app
from mito.services import user_bucket_service


def render_articles_home_layout():
    with app.app_context():
        return render_template('articles_page/home_layout.html')


def render_articles_home_action_buttons():
    with app.app_context():
        return render_template('articles_page/articles_home_actions.html')


def render_layout():
    with app.app_context():
        return render_template('articles_page/layout.html')


def render_articles(user_id, bucket_name):
    articles, error = user_bucket_service.get_articles_from_bucket(user_id, bucket_name)
    with app.app_context():
        return render_template('articles_page/articles.html', articles=articles)


def render_articles_action_buttons():
    with app.app_context():
        return render_template('articles_page/articles_actions.html')

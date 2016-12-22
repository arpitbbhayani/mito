from flask import render_template

from mito import app


def render_layout():
    with app.app_context():
        return render_template('article_page/layout.html')


def render_action_buttons():
    with app.app_context():
        return render_template('article_page/article_actions.html')


def render_article(article):
    with app.app_context():
        return render_template('article_page/article.html', article=article)

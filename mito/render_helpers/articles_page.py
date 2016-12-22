from flask import render_template

from mito import app


def render_layout():
    with app.app_context():
        return render_template('articles_page/layout.html')


def render_pending_articles(articles):
    with app.app_context():
        return render_template('articles_page/pending_articles.html', articles=articles)


def render_pending_articles_action_buttons():
    with app.app_context():
        return render_template('articles_page/pending_articles_actions.html')

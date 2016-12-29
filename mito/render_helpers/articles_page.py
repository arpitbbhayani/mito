from flask import render_template

from mito import app


def render_layout():
    with app.app_context():
        return render_template('articles_page/layout.html')


def render_articles(user_id, articles):
    with app.app_context():
        return render_template('articles_page/articles.html', articles=articles)


def render_articles_action_buttons(article_state):
    with app.app_context():
        return render_template('articles_page/articles_actions.html', article_state=article_state)

from flask import render_template

from mito import app


def render_pending_articles():
    with app.app_context():
        return render_template('articles_page/pending_articles.html')


def render_layout():
    with app.app_context():
        return render_template('dashboard_page/layout.html')

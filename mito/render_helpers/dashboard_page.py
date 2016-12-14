from flask import render_template

from mito import app


def render_dat():
    with app.app_context():
        return render_template('dashboard_page/daily_activity_tracker.html')


def render_layout():
    with app.app_context():
        return render_template('dashboard_page/layout.html')

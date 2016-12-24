from flask import render_template

from mito import app


def render_layout():
    with app.app_context():
        return render_template('companies_page/layout.html')


def render_companies(companies):
    with app.app_context():
        return render_template('companies_page/companies.html', companies=companies)


def render_companies_action_buttons():
    with app.app_context():
        return render_template('companies_page/companies_actions.html')

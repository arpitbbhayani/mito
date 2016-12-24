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


def render_company_add_form():
    with app.app_context():
        return render_template('companies_page/company_add_form.html')


def render_layout_company_add():
    with app.app_context():
        return render_template('companies_page/company_add_form_layout.html')


def render_company_edit_form(company):
    with app.app_context():
        return render_template('companies_page/company_edit_form.html', company=company)


def render_layout_company_edit():
    with app.app_context():
        return render_template('companies_page/company_edit_form_layout.html')

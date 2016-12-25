from flask import render_template, jsonify

from mito import app
from mito.services import company_service


def render_layout():
    with app.app_context():
        return render_template('companies_page/layout.html')


def render_active_companies():
    with app.app_context():
        companies, error = company_service.get_all_active_companies()
        if error:
            return jsonify(error.jsonify())
        return render_template('companies_page/companies.html', companies=companies)


def render_all_companies():
    with app.app_context():
        companies, error = company_service.get_all_companies()
        if error:
            return jsonify(error.jsonify())
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


def render_company_edit_form(company_name):
    with app.app_context():
        company, error = company_service.get_by_name(company_name)
        if error:
            return jsonify(error.jsonify())
        return render_template('companies_page/company_edit_form.html', company=company)


def render_layout_company_edit():
    with app.app_context():
        return render_template('companies_page/company_edit_form_layout.html')

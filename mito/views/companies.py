from flask import Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito.render_helpers import common_page, companies_page
from mito.entities import Company
from mito.services import company_service

mod = Blueprint('companies', __name__, )


@mod.route('/', methods=["GET"])
@login_required
def index():
    companies, error = company_service.get_all_companies()
    if error:
        return jsonify(error.jsonify())
    return LayoutSR(
        Component('companies-actions', companies_page.render_companies_action_buttons),
        Component('companies', companies_page.render_companies, companies=companies),
        layout=Layout(companies_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response


@mod.route('/add', methods=["GET", "POST"])
@login_required
def add_company():
    if request.method == 'GET':
        return LayoutSR(
            Component('company-add-form', companies_page.render_company_add_form),
            layout=Layout(companies_page.render_layout_company_add),
            pre_stream=(Dom(common_page.render_pre_body),
                        Dom(common_page.render_top_menu, current_user.is_authenticated)),
            post_stream=Dom(common_page.render_post_body)
        ).response

    company_name = request.form.get('company_name')
    company_display_name = request.form.get('display_name')
    company_icon64 = request.form.get('icon64')
    company_icon256 = request.form.get('icon256')

    company = Company(name=company_name, display_name=company_display_name,
                      icon64=company_icon64, icon256=company_icon256,
                      is_active=True)
    company, error = company_service.create_company(company)

    if error:
        flash(error.description, 'error')

    return redirect(url_for('companies.index'))


@mod.route('/edit/<company_name>', methods=["GET", "POST"])
@login_required
def edit_company(company_name):
    if request.method == 'GET':
        company, error = company_service.get_by_name(company_name)
        print(company)
        if error:
            return jsonify(error.jsonify())

        return LayoutSR(
            Component('company-edit-form', companies_page.render_company_edit_form, company),
            layout=Layout(companies_page.render_layout_company_edit),
            pre_stream=(Dom(common_page.render_pre_body),
                        Dom(common_page.render_top_menu, current_user.is_authenticated)),
            post_stream=Dom(common_page.render_post_body)
        ).response

    company_display_name = request.form.get('display_name')
    company_icon64 = request.form.get('icon64')
    company_icon256 = request.form.get('icon256')
    company_is_active = request.form.get('is_active') or False

    if company_is_active == 'on':
        company_is_active = True

    company = Company(name=company_name, display_name=company_display_name,
                      icon64=company_icon64, icon256=company_icon256,
                      is_active=company_is_active)

    company, error = company_service.update_company(company)

    if error:
        flash(error.description, 'error')

    return redirect(url_for('companies.index'))

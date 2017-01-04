from flask import render_template

from mito import app
from mito.entities import User
from mito.services import user_service, user_subscriptions_service, company_service


def render_user_search_bar():
    with app.app_context():
        return render_template('admin/user_management_page/user_search.html')


def render_user_profile_edit_form(user_email):
    with app.app_context():
        if user_email is None:
            return ""

        user, error = user_service.get_by_email(user_email)
        if error:
            return error.description

        if user is None:
            return "User %s does not exists" % (user_email)

        return render_template('admin/user_management_page/user_profile_edit_form.html', user=user, roles=User.valid_roles)


def render_user_subscriptions(user_email):
    with app.app_context():
        if user_email is None:
            return ""

        user, error = user_service.get_by_email(user_email)
        if error:
            return error.description

        if user is None:
            return "User %s does not exists" % (user_email)

        user_subscription, error = user_subscriptions_service.get_subscriptions_for_user(user.id)
        if error:
            return error.description

        user_subscription.companies = []
        for company_id in user_subscription.company_ids:
            company, error = company_service.get_by_id(company_id)
            user_subscription.companies.append(company)

        return render_template('admin/user_management_page/user_subscriptions.html', user_subscription=user_subscription)


def render_layout():
    with app.app_context():
        return render_template('admin/user_management_page/layout.html')

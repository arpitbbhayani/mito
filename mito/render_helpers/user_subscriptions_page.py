from flask import render_template

from mito import app
from mito.services import user_subscriptions_service, company_service


def render_user_subscriptions_action_buttons():
    with app.app_context():
        return render_template('user_subscriptions_page/user_subscriptions_actions.html')


def render_user_subscription(user_id):
    with app.app_context():
        user_subscription, error = user_subscriptions_service.get_subscriptions_for_user(user_id)
        if error:
            return error.description

        user_subscription.companies = []
        for company_id in user_subscription.company_ids:
            company, error = company_service.get_by_id(company_id)
            user_subscription.companies.append(company)

        return render_template('user_subscriptions_page/user_subscriptions.html', user_subscription=user_subscription)


def render_user_unsubscribed_companies(user_id):
    with app.app_context():
        user_subscription, error = user_subscriptions_service.get_subscriptions_for_user(user_id)
        if error:
            return error.description

        companies, error = company_service.get_all_active_companies()
        if error:
            return error.description

        unsubscribed_companies = [company for company in companies
                                  if company.id not in
                                  set(user_subscription.company_ids)]

        return render_template('user_subscriptions_page/user_unsubscribed_companies.html', unsubscribed_companies=unsubscribed_companies)


def render_layout():
    with app.app_context():
        return render_template('user_subscriptions_page/layout.html')

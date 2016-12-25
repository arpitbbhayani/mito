from flask import Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito.render_helpers import common_page, user_subscriptions_page
from mito.entities import UserSubscription
from mito.services import user_subscriptions_service

mod = Blueprint('user_subscriptions', __name__, )


@mod.route('/', methods=["GET"])
@login_required
def index():
    return LayoutSR(
        Component('user-subscription-actions', user_subscriptions_page.render_user_subscriptions_action_buttons),
        Component('user-subscriptions', user_subscriptions_page.render_user_subscription, current_user.id),
        Component('unsubscribed-companies', user_subscriptions_page.render_user_unsubscribed_companies, current_user.id),
        layout=Layout(user_subscriptions_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response


@mod.route('/create', methods=["POST"])
@login_required
def create_subscription():
    user_id = current_user.id
    user_subscription = UserSubscription(user_id=user_id, company_ids=[])
    user_subscription, error = user_subscriptions_service.create_user_subscription(user_subscription)

    if error:
        return jsonify(error.jsonify())

    return redirect(url_for('user_subscriptions.index'))

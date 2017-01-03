from flask import Blueprint, request
from flask_login import login_required, current_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito.render_helpers import common_page
from mito.render_helpers.admin import user_management_page
from mito.entities import User
from mito.services import user_service

mod = Blueprint('user_management', __name__, )


@mod.route('/', methods=["GET"])
@login_required
def index():
    user_email = request.args.get('email')

    return LayoutSR(
        Component('user-search-bar', user_management_page.render_user_search_bar),
        Component('user-profile-edit-form', user_management_page.render_user_profile_edit_form, user_email=user_email),
        Component('user-subscriptions', user_management_page.render_user_subscriptions, user_email=user_email),
        layout=Layout(user_management_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response

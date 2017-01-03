from flask import Blueprint, request
from flask_login import login_required, current_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito.render_helpers import common_page, user_page
from mito.entities import User
from mito.services import user_service

mod = Blueprint('user', __name__, )


@mod.route('/', methods=["GET"])
@login_required
def index():
    return LayoutSR(
        Component('user-actions', user_page.render_user_action_buttons),
        Component('user-profile', user_page.render_user_profile, current_user.id),
        layout=Layout(user_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response

from flask import Blueprint
from flask_login import login_required, current_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito.render_helpers import common_page, companies_page

mod = Blueprint('companies', __name__, )


@mod.route('/', methods=["GET"])
@login_required
def index():
    companies = []
    return LayoutSR(
        Component('companies-actions', companies_page.render_companies_action_buttons),
        Component('companies', companies_page.render_companies, companies=companies),
        layout=Layout(companies_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response

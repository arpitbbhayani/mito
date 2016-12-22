from flask import Blueprint
from flask_login import login_required, current_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito.render_helpers import common_page, articles_page

mod = Blueprint('articles', __name__, )


@mod.route('/', methods=["GET"])
@login_required
def index():
    articles = []
    return LayoutSR(
        Component('pending-articles-actions', articles_page.render_pending_articles_action_buttons),
        Component('pending-articles', articles_page.render_pending_articles, articles=articles),
        layout=Layout(articles_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response

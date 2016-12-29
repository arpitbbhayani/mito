from flask import Blueprint
from flask_login import login_required, current_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito.render_helpers import common_page, articles_page

mod = Blueprint('articles', __name__, )


@mod.route('/', methods=["GET"])
@login_required
def index():
    return LayoutSR(
        Component('articles-home-actions', articles_page.render_articles_home_action_buttons),
        layout=Layout(articles_page.render_articles_home_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response


@mod.route('/<article_state>', methods=["GET"])
@login_required
def get_articles_by_state(article_state):
    return LayoutSR(
        Component('articles-actions', articles_page.render_articles_action_buttons),
        Component('articles', articles_page.render_articles, current_user.id, article_state),
        layout=Layout(articles_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response


@mod.route('/unread/populate', methods=["POST"])
@login_required
def populate_by_state():
    return jsonify(count=0)

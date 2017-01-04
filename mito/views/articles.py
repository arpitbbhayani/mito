from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito.decorators import roles_required
from mito.render_helpers import common_page, articles_page
from mito.services import user_bucket_service

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


@mod.route('/<bucket_name>', methods=["GET"])
@login_required
def get_articles_from_bucket(bucket_name):
    return LayoutSR(
        Component('articles-actions', articles_page.render_articles_action_buttons),
        Component('articles', articles_page.render_articles, current_user.id, bucket_name),
        layout=Layout(articles_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response


@mod.route('/unread/populate', methods=["POST"])
@login_required
def populate_from_bucket():
    """Takes articles from recommended into puts them into unread
    """
    user_id = current_user.id
    actual_moved, error = user_bucket_service.move_articles(user_id, 'recommended', 'unread', count=5)
    return redirect(url_for('articles.index'))


@mod.route('/recommended/populate/<user_id>', methods=["POST"])
@login_required
@roles_required('admin')
def recommend_articles(user_id):
    return jsonify(count=0)

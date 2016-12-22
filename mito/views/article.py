from flask import Blueprint
from flask_login import login_required, current_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito.render_helpers import article_page, common_page

mod = Blueprint('article', __name__, )


@mod.route('/<article_id>', methods=["GET"])
@login_required
def get_note(article_id):
    return "Article for id: " + article_id


@mod.route('/<article_id>/redirect', methods=["GET"])
@login_required
def redirect_to_original():
    return "Redirecting article to original source article"


@mod.route('/<article_id>/mark/read', methods=["POST"])
@login_required
def mark_article_read():
    return "Mark article as read"


@mod.route('/<article_id>/mark/bookmark', methods=["POST"])
@login_required
def mark_article_bookmark():
    return "Mark article as bookmark"


@mod.route('/<article_id>/mark/like', methods=["POST"])
@login_required
def mark_article_as_liked():
    return "Mark article as liked"

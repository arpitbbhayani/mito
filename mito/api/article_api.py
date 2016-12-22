from flask import Blueprint

mod = Blueprint('article_api', __name__, )


@mod.route('/create', methods=["PUT"])
def create_article():
    return "Create article"


@mod.route('/update/<article_id>', methods=["POST"])
def update_article(article_id):
    return "Update article"

from flask import Blueprint, request, jsonify

from mito.entities import Article
from mito.services import article_service

mod = Blueprint('article_api', __name__, )


@mod.route('/create', methods=["POST"])
def create_article():
    article = Article(**request.json)
    article, error = article_service.create_article(article)
    if error:
        return jsonify(error.jsonify())
    return jsonify(article.__dict__)


@mod.route('/update/<article_id>', methods=["POST"])
def update_article(article_id):
    return "Update article"

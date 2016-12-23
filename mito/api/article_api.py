from flask import Blueprint, request, jsonify

from mito.errors import MitoError
from mito.entities import Article
from mito.dao import ArticleDao

mod = Blueprint('article_api', __name__, )


@mod.route('/create', methods=["POST"])
def create_article():
    article = Article(**request.json)
    try:
        article = ArticleDao.create(article)
    except MitoError as m:
        return jsonify(m.jsonify())
    else:
        return jsonify(article.__dict__)


@mod.route('/update/<article_id>', methods=["POST"])
def update_article(article_id):
    return "Update article"

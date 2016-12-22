from flask import Blueprint, request, jsonify

from mito.entities import Article
from mito.dao import ArticleDao

mod = Blueprint('article_api', __name__, )


@mod.route('/create', methods=["POST"])
def create_article():
    article = Article(**request.json)
    article = ArticleDao.create(article)
    return jsonify(article.__dict__)


@mod.route('/update/<article_id>', methods=["POST"])
def update_article(article_id):
    return "Update article"

from mito.dao import ArticleDao
from mito.errors import MitoError


def create_article(article):
    article, error = None, None
    try:
        article = ArticleDao.create(article)
    except MitoError as m:
        error = m
    return article, error

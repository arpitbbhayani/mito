from mito.entities import Article
from mito.errors import DuplicateDataError
from mito.distributed_db.api import index as index_api
from mito.distributed_db.api import data as data_api


class ArticleDao:
    @staticmethod
    def create(article):
        link = article.link
        existing_article = index_api.get_one(Article, 'link', link)
        if existing_article:
            raise DuplicateDataError("Article with link '%s' already exists!" % (link))

        return data_api.add(article)

    @staticmethod
    def update(article):
        print("Updating the article")

    @staticmethod
    def get_by_id(guid):
        return data_api.get(Article, guid)

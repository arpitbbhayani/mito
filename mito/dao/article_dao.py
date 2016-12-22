from mito.entities import Article
from mito.distributed_db.api import index as index_api
from mito.distributed_db.api import data as data_api


class ArticleDao:
    @staticmethod
    def create(article):
        return data_api.add(article)

    @staticmethod
    def update(article):
        print("Updating the article")

    @staticmethod
    def get_by_id(guid):
        return data_api.get(Article, guid)

    # @staticmethod
    # def get_by_date(date):
    #     article = index_api.get_one(Article, 'dated', date)
    #     return note

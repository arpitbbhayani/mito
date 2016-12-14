from mito.entities import User
from mito.distributed_db.guid import GUID
from mito.distributed_db.api import index as index_api
from mito.distributed_db.api import data as data_api


class UserDao:
    @staticmethod
    def create(user):
        return data_api.add(user)

    @staticmethod
    def update(record):
        print("Updating the record")

    @staticmethod
    def get_by_id(guid):
        return data_api.get(User, guid)

    @staticmethod
    def get_by_email(email):
        user = index_api.get_one(User, 'email', email)
        return user

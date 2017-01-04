from mito.entities import User
from mito.distributed_db.api import index as index_api
from mito.distributed_db.api import data as data_api


class UserDao:
    @staticmethod
    def create(user):
        email = user.email
        existing_user = index_api.get_one(User, 'email', email)
        if existing_user:
            raise DuplicateDataError("User with email '%s' already exists!" % (email))

        return data_api.add(user)

    @staticmethod
    def update(user):
        db_user = data_api.get(User, user.id)
        db_user.__dict__.update(user.__dict__)
        return data_api.update(db_user)

    @staticmethod
    def get_by_id(guid):
        return data_api.get(User, guid)

    @staticmethod
    def get_by_email(email):
        user = index_api.get_one(User, 'email', email)
        return user

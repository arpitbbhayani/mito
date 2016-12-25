from mito.entities import UserSubscription
from mito.errors import DuplicateDataError
from mito.distributed_db.api import index as index_api
from mito.distributed_db.api import data as data_api


class UserSubscriptionDao:
    @staticmethod
    def get_by_userid(user_id):
        return index_api.get_one(UserSubscription, 'user_id', user_id, is_list=False)

    @staticmethod
    def create(user_subscription):
        user_id = user_subscription.user_id
        existing_user_subscription = index_api.get_one(UserSubscription, 'user_id', user_id, is_list=False)
        if existing_user_subscription:
            raise DuplicateDataError("User subscription for user '%s' already exists!" % (user_id))

        return data_api.add(user_subscription)

    @staticmethod
    def update(user_subscription):
        db_user_subscription = data_api.get(UserSubscription, user_subscription.id)
        db_user_subscription.__dict__.update(user_subscription.__dict__)
        return data_api.update(db_user_subscription)

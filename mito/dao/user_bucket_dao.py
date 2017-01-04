from mito.entities import UserBucket
from mito.errors import DuplicateDataError
from mito.distributed_db.api import index as index_api
from mito.distributed_db.api import data as data_api


class UserBucketDao:
    @staticmethod
    def get_by_userid(user_id):
        return index_api.get_one(UserBucket, 'user_id', user_id, is_list=False)

    @staticmethod
    def get_article_ids_from_bucket(user_id, bucket_name, count=5):
        projection = {
            bucket_name: {'$slice': count}
        }
        return index_api.get_one(UserBucket, 'user_id', user_id, is_list=False, projection=projection)

    @staticmethod
    def create(user_bucket):
        user_id = user_bucket.user_id
        existing_user_bucket = index_api.get_one(UserBucket, 'user_id', user_id, is_list=False)
        if existing_user_bucket:
            raise DuplicateDataError("User bucket for user '%s' already exists!" % (user_id))

        return data_api.add(user_bucket)

    @staticmethod
    def update(user_bucket):
        db_user_bucket = data_api.get(UserBucket, user_bucket.id)
        db_user_bucket.__dict__.update(user_bucket.__dict__)
        return data_api.update(user_bucket)

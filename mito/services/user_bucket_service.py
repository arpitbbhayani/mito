from mito.dao import UserSubscriptionDao, UserBucketDao
from mito.errors import MitoError, EntityNotFoundError


def get_articles_by_state(user_id, article_state, count=5):
    error = None
    try:
        user_bucket = UserBucketDao.get_article_ids_by_state(user_id, article_state, count=count)
    except MitoError as m:
        error = m
    return user_bucket, error


def get_bucket_for_user(user_id):
    error = None
    try:
        user_bucket = UserBucketDao.get_by_userid(user_id)
    except MitoError as m:
        error = m
    return user_bucket, error


def create_user_bucket(user_bucket):
    error = None
    try:
        user_bucket = UserBucketDao.create(user_bucket)
    except MitoError as m:
        error = m
    return user_bucket, error


def add_article_to_bucket(user_id, bucket_name, article_id):
    error = None
    try:
        user_bucket = UserBucketDao.get_by_userid(user_id)
        if user_bucket is None:
            raise EntityNotFoundError("User bucket for user '%s' not found" % (user_id))

        old_count = len(user_bucket[bucket_name])

        user_bucket.__dict__[bucket_name] = list(set(user_bucket.__dict__[bucket_name] + [article_id]))
        user_bucket = UserBucketDao.update(user_bucket)

        is_added = old_count != len(user_bucket.__dict__[bucket_name])
    except MitoError as m:
        error = m
    return is_added, error


def remove_article_from_bucket(user_id, bucket_name, article_id):
    error = None
    try:
        user_bucket = UserBucketDao.get_by_userid(user_id)
        if user_bucket is None:
            raise EntityNotFoundError("User bucket for user '%s' not found" % (user_id))

        old_count = len(user_bucket[bucket_name])

        try:
            user_bucket.__dict__[bucket_name] = list(set(user_bucket.__dict__[bucket_name].remove(article_id)))
            user_bucket = UserBucketDao.update(user_bucket)
        except KeyError as e:
            is_removed = False
        else:
            is_removed = True
    except MitoError as m:
        error = m

    return is_removed, error

from mito.dao import UserSubscriptionDao, UserBucketDao
from mito.errors import MitoError, EntityNotFoundError, MitoTypeError


def get_articles_from_bucket(user_id, bucket_name, count=5):
    error = None
    try:
        user_bucket = UserBucketDao.get_article_ids_from_bucket(user_id, bucket_name, count=count)
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


def add_articles_to_bucket(user_id, bucket_name, article_ids):
    error = None
    try:
        if type(article_ids) != list or type(article_ids) != set:
            raise MitoTypeError("article_ids should be a List or a Set")

        user_bucket = UserBucketDao.get_by_userid(user_id)
        if user_bucket is None:
            raise EntityNotFoundError("User bucket for user '%s' not found" % (user_id))

        old_count = len(user_bucket[bucket_name])

        user_bucket.__dict__[bucket_name] = list(set(user_bucket.__dict__[bucket_name] + set(article_ids)))
        user_bucket = UserBucketDao.update(user_bucket)

        move_count = len(user_bucket.__dict__[bucket_name]) - old_count
    except MitoError as m:
        error = m
    return move_count, error


def remove_article_from_bucket(user_id, bucket_name, article_id):
    error = None
    try:
        user_bucket = UserBucketDao.get_by_userid(user_id)
        if user_bucket is None:
            raise EntityNotFoundError("User bucket for user '%s' not found" % (user_id))

        old_count = len(user_bucket.__dict__[bucket_name])

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


def move_articles(user_id, source_bucket_name, destination_bucket_name, count=5):
    error = None
    article_count = 0

    try:
        user_bucket = UserBucketDao.get_by_userid(user_id)
        if user_bucket is None:
            raise EntityNotFoundError("User bucket for user '%s' not found" % (user_id))

        if source_bucket_name not in user_bucket.__dict__:
            raise EntityNotFoundError("Bucket '%s' does not exist" % (source_bucket_name))

        if destination_bucket_name not in user_bucket.__dict__:
            raise EntityNotFoundError("Bucket '%s' does not exist" % (destination_bucket_name))

        old_count = len(user_bucket.__dict__[destination_bucket_name])

        articles_to_move = user_bucket.__dict__[source_bucket_name][count:]
        article_list = user_bucket.__dict__[source_bucket_name][:count]

        user_bucket.__dict__[destination_bucket_name] = list(set(user_bucket.__dict__[destination_bucket_name] + articles_to_move))
        user_bucket.__dict__[source_bucket_name] = article_list

        article_count = len(user_bucket.__dict__[destination_bucket_name]) - old_count

    except MitoError as m:
        error = m

    return article_count, error

from mito.services import user_bucket_service


def get_recommended_articles(user_id, count=5):
    return first_unprocessed(user_id, count)


def first_unprocessed(user_id, count):
    return []


def recommend_articles(user_id):
    article_ids = get_recommended_articles(user_id)
    move_count, error = user_bucket_service.add_articles_to_bucket(user_id, 'recommended', article_ids)
    return move_count, error

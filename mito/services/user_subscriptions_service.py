from mito.dao import UserSubscriptionDao
from mito.errors import MitoError


def get_subscriptions_for_user(user_id):
    error = None
    try:
        user_subscription = UserSubscriptionDao.get_by_userid(user_id)
    except MitoError as m:
        error = m
    return user_subscription, error


def create_user_subscription(user_subscription):
    error = None
    try:
        user_subscription = UserSubscriptionDao.create(user_subscription)
    except MitoError as m:
        error = m
    return user_subscription, error

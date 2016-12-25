from mito.dao import UserSubscriptionDao, CompanyDao
from mito.errors import MitoError, EntityNotFoundError


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


def subscribe(user_id, company_id):
    error = None
    try:
        company = CompanyDao.get_by_id(company_id)
        if company is None:
            raise EntityNotFoundError("Company with id '%s' not found" % (company_id))

        user_subscription = UserSubscriptionDao.get_by_userid(user_id)
        if user_subscription is None:
            raise EntityNotFoundError("User subscription for user '%s' not found" % (user_id))

        user_subscription.company_ids = list(set(user_subscription.company_ids + [company_id]))
        user_subscription = UserSubscriptionDao.update(user_subscription)
    except MitoError as m:
        error = m
    return user_subscription, error

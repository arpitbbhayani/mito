from mito.dao import UserDao
from mito.errors import MitoError


def create_user(user):
    error = None
    try:
        user = UserDao.create(user)
    except MitoError as m:
        error = m
    return user, error


def update_user(user_id, **kwargs):
    error = None
    try:
        user = UserDao.get_by_id(user_id)
        user.__dict__.update(kwargs)
        user = UserDao.update(user)
    except MitoError as m:
        error = m
    return user, error


def get_by_id(user_id):
    error = None
    try:
        user = UserDao.get_by_id(user_id)
    except MitoError as m:
        error = m
    return user, error


def get_by_email(email):
    error = None
    try:
        user = UserDao.get_by_email(email)
    except MitoError as m:
        error = m
    return user, error

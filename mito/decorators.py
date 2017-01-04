from flask import abort
from flask_login import current_user

from functools import wraps


def roles_required(*expected_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_roles = current_user.roles or None
            if set(expected_roles) - set(user_roles):
                abort(400)
            return func(*args, **kwargs)
        return wrapper
    return decorator

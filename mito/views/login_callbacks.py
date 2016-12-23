from flask import Blueprint, abort, url_for, session, redirect
from flask_login import login_user

from mito import github
from mito.services import user_service
from mito.entities import User

mod = Blueprint('login_callbacks', __name__, )


@mod.route('/github', methods=["GET"])
@github.authorized_handler
def github_login_callback(oauth_token):
    next_url = url_for('pages.index')
    if oauth_token is None:
        abort(403, "Authorization failed.")

    session['github_access_token'] = oauth_token
    emails = github.get('user/emails')

    user_email = emails[0]['email']
    user, error = user_service.get_by_email(user_email)

    if error:
        raise error

    if user is None:
        user = User(email=user_email)
        user, error = user_service.create_user(user)

        if error:
            raise error

    login_user(user)
    return redirect(next_url)


@github.access_token_getter
def token_getter():
    return session.get('github_access_token')

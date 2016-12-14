from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from mito import github

mod = Blueprint('pages', __name__, )


@mod.route('/', methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('pages.dashboard'))
    return render_template('index.html')


@mod.route('/login', methods=["GET"])
def login():
    return github.authorize('user:email')


@mod.route('/dashboard', methods=["GET"])
@login_required
def dashboard():
    return "User Dashboard"

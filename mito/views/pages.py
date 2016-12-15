from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user, logout_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito import github
from mito.render_helpers import index_page, common_page, dashboard_page

mod = Blueprint('pages', __name__, )


@mod.route('/', methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('pages.dashboard'))

    return LayoutSR(
        Component('main-content', index_page.render_main_content),
        layout=Layout(index_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response


@mod.route('/login', methods=["GET"])
def login():
    return github.authorize('user:email')


@mod.route('/logout', methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for('pages.index'))


@mod.route('/dashboard', methods=["GET"])
@login_required
def dashboard():
    return LayoutSR(
        Component('notes', dashboard_page.render_dat),
        layout=Layout(dashboard_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, is_authenticated=current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response

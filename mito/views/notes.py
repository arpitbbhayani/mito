from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user, logout_user
from flasksr import LayoutSR, Component, Dom, Layout

from mito import github
from mito.render_helpers import notes_page, common_page

mod = Blueprint('notes', __name__, )


@mod.route('/<note_id>', methods=["GET"])
@login_required
def get_note():
    return ""


@mod.route('/', methods=["GET"])
@login_required
def index():
    notes = []
    return LayoutSR(
        Component('notes-actions', notes_page.render_action_buttons),
        Component('notes', notes_page.render_notes, notes=notes),
        layout=Layout(notes_page.render_layout),
        pre_stream=(Dom(common_page.render_pre_body),
                    Dom(common_page.render_top_menu, current_user.is_authenticated)),
        post_stream=Dom(common_page.render_post_body)
    ).response


@mod.route('/new', methods=["GET", "POST"])
@login_required
def create_note():
    if request.method == 'GET':
        return "New note"

    if request.method == 'POST':
        print(request.form)
        return "New note saved"


@mod.route('/<note_id>/delete', methods=["POST"])
@login_required
def delete_note():
    return ""


@mod.route('/<note_id>', methods=["POST"])
@login_required
def save_note():
    return ""

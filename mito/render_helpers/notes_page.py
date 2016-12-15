from flask import render_template

from mito import app


def render_layout():
    with app.app_context():
        return render_template('notes_page/layout.html')


def render_action_buttons():
    with app.app_context():
        return render_template('notes_page/notes_actions.html')


def render_notes(notes):
    with app.app_context():
        return render_template('notes_page/notes.html', notes=notes)

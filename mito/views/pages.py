from flask import Blueprint, render_template

mod = Blueprint('pages', __name__, )


@mod.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

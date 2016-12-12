from flask import Blueprint, jsonify

mod = Blueprint('status', __name__, )


@mod.route('/', methods=["GET"])
def index():
    return jsonify(status='OK')

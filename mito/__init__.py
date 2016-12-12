import os
from flask import Flask

app = Flask(__name__)

"""
Load default settings from file `defaults.py`
"""
app.config.from_object('mito.defaults')

"""
Overriding default settings from Environment variables.
"""
overridden_config = {k:v for k, v in os.environ.items() if k in app.config}
app.config.update(overridden_config)

"""
Registering all blueprints.
"""
from mito.views import pages, status

app.register_blueprint(pages.mod)
app.register_blueprint(status.mod, url_prefix='/status')

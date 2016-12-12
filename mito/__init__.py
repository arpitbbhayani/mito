from flask import Flask

app = Flask(__name__)

from mito.views import pages, status

app.register_blueprint(pages.mod)
app.register_blueprint(status.mod, url_prefix='/status')

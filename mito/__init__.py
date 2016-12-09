from flask import Flask

app = Flask(__name__)

from mito.views import pages
app.register_blueprint(pages.mod)

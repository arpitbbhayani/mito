import os
import sys
import json
from flask import Flask
from flask_github import GitHub

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
Configure the database map
"""
from mito.distributed_db import create_mongo_clients, create_mongo_meta_client
mongo_clients = create_mongo_clients(json.loads(app.config['DB_JSON']))
mongo_meta_client = create_mongo_meta_client(json.loads(app.config['META_DB_JSON']))

if len(mongo_clients) == 0:
    print("No mongoDB configured! Check your environment varaibled 'DB_JSON'")
    sys.exit(1)

"""
Create Indexes in all of MongoDB instances
"""
from mito import db_init

db_init.create_indexes()

"""
Session based Flask login initialization
"""
from flask_login import LoginManager
from mito.dao import UserDao

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_user = UserDao.get_by_id(user_id)
    return db_user

"""
Github based login initialization
"""
github = GitHub(app)

"""
Registering all blueprints.
"""
from mito.views import pages, status, login_callbacks, articles, article

app.register_blueprint(pages.mod)
app.register_blueprint(status.mod, url_prefix='/status')
app.register_blueprint(login_callbacks.mod, url_prefix='/callback/login')
app.register_blueprint(articles.mod, url_prefix='/articles')
app.register_blueprint(article.mod, url_prefix='/article')


"""
Registering all APIs
"""
from mito.api import article_api

app.register_blueprint(article_api.mod, url_prefix='/api/article')

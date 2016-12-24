from mito import mongo_meta_client
from mito.distributed_db.utils import get_index_collection_name, get_mongo_shard_client
from mito.distributed_db.api import data as data_api

def add(obj):
    for attr in obj.__indexed_attrs__:
        value = getattr(obj, attr)
        if value is not None:
            collection_name = get_index_collection_name(obj.__class__, attr)
            client = mongo_meta_client
            db = client.indexdb
            if type(value) is list:
                db[collection_name].update({'_id': obj.id}, {'$addToSet': {"value": {"$each": value}}}, upsert=True)
            else:
                db[collection_name].update({'_id': obj.id}, {'$set': {"value": value}}, upsert=True)


def delete(obj):
    for attr in obj.__indexed_attrs__:
        value = getattr(obj, attr)
        if value is not None:
            collection_name = get_index_collection_name(obj.__class__, attr)
            client = mongo_meta_client
            db = client['indexdb']
            db[collection_name].remove({'_id': obj.id})


def get_one(cls, attr, value):
    client = mongo_meta_client
    collection_name = get_index_collection_name(cls, attr)
    db = client['indexdb']
    db_user = db[collection_name].find_one({"values": {"$in": [value]}})

    if db_user is None:
        return None

    return data_api.get(cls, db_user['_id'])


def update(obj):
    delete(obj)
    add(obj)

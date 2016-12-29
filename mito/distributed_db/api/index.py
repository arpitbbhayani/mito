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


def get_one(cls, attr, value, is_list=False, projection=None):
    client = mongo_meta_client
    collection_name = get_index_collection_name(cls, attr)
    db = client['indexdb']

    if is_list:
        db_entity = db[collection_name].find_one({"value": {"$in": [value]}})
    else:
        db_entity = db[collection_name].find_one({"value": value})

    if db_entity is None:
        return None

    return data_api.get(cls, db_entity['_id'], projection=projection)


def get_all(cls, attr, value, is_list=False):
    client = mongo_meta_client
    collection_name = get_index_collection_name(cls, attr)
    db = client['indexdb']

    if is_list:
        db_entities = db[collection_name].find({"value": {"$in": [value]}})
    else:
        db_entities = db[collection_name].find({"value": value})

    return [data_api.get(cls, db_entity['_id']) for db_entity in db_entities]


def update(obj):
    delete(obj)
    add(obj)

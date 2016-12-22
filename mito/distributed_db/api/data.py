from bson.objectid import ObjectId
from mito.distributed_db import GUID
from mito.distributed_db.api import index as index_api
from mito.distributed_db.utils import get_mongo_shard_client, get_mongo_shard_client_by_dbindex


def add(data):
    client, dbindex = get_mongo_shard_client(data)
    result = client.mitodb[data.__discriminator__].insert_one(data.__dict__)
    data.id = GUID.encode(dbindex, data.__discriminator__, result.inserted_id)
    index_api.add(data)

    del data._id
    return data


def update(data):
    dbindex, collection_name, document_id = GUID.decode(data.id)
    client = get_mongo_shard_client_by_dbindex(dbindex)
    result = client.mitodb[data.__discriminator__].update({'_id': document_id}, data.__dict__)
    index_api.update(data)
    return data


def delete(data):
    dbindex, collection_name, document_id = GUID.decode(data.id)
    client = get_mongo_shard_client_by_dbindex(dbindex)
    result = client.mitodb[data.__discriminator__].remove({'_id': document_id})
    index_api.delete(data)
    return True


def get(cls, guid):
    dbindex, collection_name, document_id = GUID.decode(guid)
    client = get_mongo_shard_client_by_dbindex(dbindex)
    data = client.mitodb[cls.__discriminator__].find_one({'_id': ObjectId(document_id)})

    if data is None:
        return None

    obj = cls.from_dict(data)
    obj.id = guid
    return obj

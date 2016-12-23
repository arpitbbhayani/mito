from mito import mongo_clients, mongo_meta_client


def get_index_collection_name(entity_class, attr):
    return "%s_%s" % (getattr(entity_class, '__discriminator__'), attr)


def get_mongo_shard_client(obj):
    shard_key_attr = obj.__shard_key__
    shard_key = str(getattr(obj, shard_key_attr))
    index = sum([ord(c) for c in shard_key]) % len(mongo_clients)
    return mongo_clients[index], index


def get_mongo_shard_client_by_dbindex(dbindex):
    return mongo_clients[int(dbindex)]


def get_all_mongo_shard_clients():
    return mongo_clients


def get_mongo_meta_client():
    return mongo_meta_client

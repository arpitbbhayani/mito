from mito.distributed_db.utils import get_mongo_meta_client, get_index_collection_name
from mito.entities import Article, User


def create_indexes():
    client = get_mongo_meta_client()
    client.indexdb[get_index_collection_name(User, 'email')].ensure_index("value", unique=True)
    client.indexdb[get_index_collection_name(Article, 'link')].ensure_index("value", unique=True)

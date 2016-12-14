from .client import create_client


def create_mongo_meta_client(meta_config):
    """Returns MongoClient from meta_config.

    The expected format of db_configs is
    {
        "host": "localhost",
        "port": 27017
    }
    """
    return create_client(meta_config['host'], meta_config['port'])


def create_mongo_clients(db_configs):
    """Returns a list of MongoClient from db_configs.

    The expected format of db_configs is
    [
        {
            "host": "localhost",
            "port": 27017
        }
    ]
    """
    return [create_client(db_config['host'], db_config['port'])
                for db_config in db_configs]

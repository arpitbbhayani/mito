from pymongo import MongoClient


def create_client(host, port):
    """Given host and port, this function returns the MongoClient Object
    """
    return MongoClient(host, port)

from bson import ObjectId


class GUID:
    @staticmethod
    def encode(db_index, collection_name, document_id):
        return "%s+%s+%s" % (db_index, collection_name, document_id)

    @staticmethod
    def decode(guid):
        db_index, collection_name, document_id = guid.split('+')
        return db_index, collection_name, ObjectId(document_id)

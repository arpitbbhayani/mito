from mito.entities import User
from mito.distributed_db.api import index as index_api
from mito.distributed_db.api import data as data_api


class NoteDao:
    @staticmethod
    def create(note):
        return data_api.add(note)

    @staticmethod
    def update(note):
        print("Updating the note")

    @staticmethod
    def get_by_id(guid):
        return data_api.get(Note, guid)

    @staticmethod
    def get_by_date(date):
        note = index_api.get_one(Note, 'dated', date)
        return note

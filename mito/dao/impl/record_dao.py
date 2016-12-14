class RecordDao:
    def __init__(self):
        pass

    def create(self, record):
        print("Creating a new record")

    def update(self, record):
        print("Updating the record")

    def get_by_id(self, id):
        print("Getting record by ID")

    def get_by_id_for_user(self, id, user):
        print("Getting record by ID for user")

    def get_records_by_user(self, user):
        print("Getting records by user")

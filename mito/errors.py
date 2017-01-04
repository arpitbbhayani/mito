class MitoError(Exception):
    def __init__(self, error_code, description):
        Exception.__init__(self)
        self.error_code = error_code
        self.description = description

    def jsonify(self):
        return {
            'error_code': self.error_code,
            'description': self.description
        }


class DuplicateDataError(MitoError):
    def __init__(self, message):
        MitoError.__init__(self, 'DUPLICATE_DATA_ERROR', message)


class EntityNotFoundError(MitoError):
    def __init__(self, message):
        MitoError.__init__(self, 'ENTITY_NOT_FOUND_ERROR', message)


class MitoTypeError(MitoError):
    def __init__(self, message):
        MitoError.__init__(self, 'ENTITY_TYPE_ERROR', message)

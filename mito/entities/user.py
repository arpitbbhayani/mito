from flask_login import UserMixin


class User(UserMixin):
    __shard_key__ = 'email'
    __discriminator__ = 'user'
    __indexed_attrs__ = ['email']
    __attrs__ = ['email']

    def __init__(self, **kwargs):
        data = {k: v for k, v in kwargs.items() if k in self.__attrs__}
        self.__dict__.update(data)

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

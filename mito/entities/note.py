class Note:
    __shard_key__ = 'dated'
    __discriminator__ = 'dated'
    __indexed_attrs__ = ['dated']
    __attrs__ = ['dated', 'body']

    def __init__(self, **kwargs):
        data = {k: v for k, v in kwargs.items() if k in self.__attrs__}
        self.__dict__.update(data)

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

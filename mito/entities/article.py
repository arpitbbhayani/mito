class Article:
    __shard_key__ = 'title'
    __discriminator__ = 'article'
    __indexed_attrs__ = ['tags', 'company', 'link']
    __attrs__ = ['title', 'body', 'tags', 'link', 'image', 'company',
                 'created_at', 'checksum']

    def __init__(self, **kwargs):
        data = {k: v for k, v in kwargs.items() if k in self.__attrs__}
        self.__dict__.update(data)

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

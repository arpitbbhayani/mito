class Company:
    __shard_key__ = 'name'
    __discriminator__ = 'company'
    __indexed_attrs__ = ['name']
    __attrs__ = ['name', 'display_name', 'icon64', 'icon256', 'blog_url']

    def __init__(self, **kwargs):
        data = {k: v for k, v in kwargs.items() if k in self.__attrs__}
        self.__dict__.update(data)

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

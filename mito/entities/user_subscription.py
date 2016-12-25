class UserSubscription:
    __shard_key__ = 'user_id'
    __discriminator__ = 'user_subscription'
    __indexed_attrs__ = ['user_id']
    __attrs__ = ['user_id', 'company_ids']

    def __init__(self, **kwargs):
        data = {k: v for k, v in kwargs.items() if k in self.__attrs__}
        self.__dict__.update(data)

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

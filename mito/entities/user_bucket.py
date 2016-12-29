class UserBucket:

    READ_BUCKET_NAME = 'read'
    UNREAD_BUCKET_NAME = 'unread'
    LIKED_BUCKET_NAME = 'liked'
    RECOMMENDED_BUCKET_NAME = 'recommended'

    __shard_key__ = 'user_id'
    __discriminator__ = 'user_bucket'
    __indexed_attrs__ = ['user_id']
    __attrs__ = ['user_id', READ_BUCKET_NAME, UNREAD_BUCKET_NAME,
                 LIKED_BUCKET_NAME, RECOMMENDED_BUCKET_NAME]

    def __init__(self, **kwargs):
        data = {k: v for k, v in kwargs.items() if k in self.__attrs__}
        self.__dict__.update(data)

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

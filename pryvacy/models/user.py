from pryvacy.models import Base
from pryvacy.utils import get_hash, verify_hash, timestamp

class User(Base):

    collection = Base.db.users

    @classmethod
    def create(cls, username, password):
        return cls.collection.insert({
            'username': username,
            'password': get_hash(password),
            'private_key': None,
            'public_key': None,
            'last_auth': timestamp()
        })

    @classmethod
    def auth(cls, username, password):
        user = cls.collection.find_one({
            '$or': [{'email': username}, {'username': username}]
        })
        if user and verify_hash(password, user['password']):
            cls.collection.update(
                {'_id': user['_id']},
                {
                    '$set': {'last_auth': timestamp()}
                }
            )
            return user

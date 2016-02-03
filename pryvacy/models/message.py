from pryvacy.models import Base
from pryvacy.utils import timestamp

class Message(Base):

    collection = Base.db.messages

    @classmethod
    def create(cls, sender, recipient, body, ip, browser):
        return cls.collection.insert({
            'sender': sender,
            'recipient': recipient,
            'body': body,
            'ip': ip,
            'browser': browser,
            'timestamp': timestamp(),
            'read': False
        })

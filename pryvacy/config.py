import os

class Config():
    SECRET_KEY = 'pryvacy'

    MAIL_SERVER = 'smtp.dummy.com'
    MAIL_PORT = '123'
    MAIL_USERNAME = 'uname'
    MAIL_PASSWORD = 'pass'
    MAIL_DEFAULT_SENDER = 'awesome@awesome.com'

    HOST = 'http://localhost:5000'

class Debug(Config):
    DEBUG = True


class Develop(Debug):
    SECRET_KEY = os.environ.get('SECRET_KEY') or Config.SECRET_KEY

    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

    HOST = os.environ.get('pryvacy_host') or Config.HOST

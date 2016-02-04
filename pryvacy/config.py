import os

class Config():
    SECRET_KEY = 'pryvacy'

    HOST = 'http://localhost:5000'

class Debug(Config):
    DEBUG = True


class Develop(Debug):
    SECRET_KEY = os.environ.get('SECRET_KEY') or Config.SECRET_KEY
    HOST = os.environ.get('pryvacy_host') or Config.HOST
    

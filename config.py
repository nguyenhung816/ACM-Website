class Config(object):
    SECRET_KEY = 'test-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ACM_member.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
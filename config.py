import os


class Config(object):
    forwarded_allow_ips = '*'
    secure_scheme_headers = {'X-Forwarded-Proto': 'https'}

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 30
    SQLALCHEMY_POOL_TIMEOUT = 30  # 30 seconds
    SQLALCHEMY_POOL_RECYCLE = 10  # max connection idle
    SQLALCHEMY_MAX_OVERFLOW = 50  # max in queue
    JSON_SORT_KEYS = False
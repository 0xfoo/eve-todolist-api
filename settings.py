# -*- coding: utf-8 -*-

user_schema = {
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 64,
        'required': True,
        'unique': True
    },
    'email': {
        'type': 'string',
        'regex': '^\S+@\S+.\S+',
        'required': True,
        'unique': True
    },
    'joined_at': {
        'type': 'datetime'
    }
}


user = {
    'item_title': 'person',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': user_schema
}

DOMAIN = {
    'user': {},
    'todolists': {},
    'todos': {}
}

# mongo db settings
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'apitest'

# RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
# ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

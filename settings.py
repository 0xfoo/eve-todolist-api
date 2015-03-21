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
    'password': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 64,
        'required': True
    },
}

user = {
    'item_title': 'user',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': user_schema
}

todolist_schema = {
    'title': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 128,
        'required': True
    },
    'creator': {
        'type': 'string'
    },
    'todos': {},
}

todolist = {
    'item_title': 'todolist',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        # 'field': '_id'
        'field': 'title'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'schema': todolist_schema
}

todo_schema = {
    'description': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 128,
        'required': True
    },
    'creator': {
        'type': 'string'
    },
    'todolist': {},
}

todo = {
    'item_title': 'todo',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        # 'field': '_id'
        'field': 'description'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'schema': todo_schema
}

DOMAIN = {
    'users': user,
    'todolists': todolist,
    'todos': todo
}

# mongo db settings
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'apitest'

#!/usr/bin/env python
# encoding: utf-8

from mongokit import *
import datetime

connection = Connection('mongodb://127.0.0.1:27017')


@connection.register
class Post(Document):
    structure = {
        'title': unicode,
        'body': unicode,
        'author': unicode,
        'date_creation': datetime.datetime,
        'rank': int
    }
    required_fields = ['title', 'author', 'date_creation']
    default_values = {'rank': 0, 'date_creation': datetime.datetime.utcnow}

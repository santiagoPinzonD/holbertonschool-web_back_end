#!/usr/bin/env python3
""" Insert """


def insert_school(mongo_collection, **kwargs):
    """ Insert """
    return mongo_collection.insert({**kwargs})

#!/usr/bin/env python3
""" All collections """


def list_all(mongo_collection):
    """ List all documents in Python"""
    return mongo_collection.find()

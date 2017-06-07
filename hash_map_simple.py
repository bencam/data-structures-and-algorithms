#!/usr/bin/env python


"""
A very simple hashing function with two methods:

1. hash_function() simply creates a hash value

2. insert() adds a given key-value pair into the hash map
"""


class HashTable(object):

    def __init__(self):
        self.table = [[] for _ in range(10)]

    def hash_function(self, key):
        return key % 10

    def insert(self, key, value):
        self.table[self.hash_function(key)].append(value)


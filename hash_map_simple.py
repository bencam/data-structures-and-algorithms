#!/usr/bin/env python


class HashTable(object):

    def __init__(self):
        self.table = [[] for _ in range(10)]

    def hash_function(self, key):
        return key % 10

    def insert(self, key, value):
        self.table[self.hash_function(key)].append(value)


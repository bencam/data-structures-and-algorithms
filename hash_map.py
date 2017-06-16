#!/usr/bin/env python


class HashMap(object):


    def __init__(self):
        """Initialize a hash map with 10,000 buckets or spots."""
        self.table = [None] * 10000


    def store(self, string):
        """Stores a string in the hash map."""
        # Give the string a hash value
        hash_value = self.calculate_hash_value(string)
        # Make sure the hash value is valid
        if hash_value != -1:
            # Is there something already in the bucket?
            if self.table[hash_value] != None:
                # If the bucket is not empty, append the string
                self.table[hash_value].append(string)
            else:
                self.table[hash_value] = [string]


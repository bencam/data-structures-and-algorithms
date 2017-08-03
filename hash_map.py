#!/usr/bin/env python


"""
A hash map implementation with one class (HashMap).

The HashMap class consists to five methods:

1. __init__() - creates a list of 10,000 buckets set to a default
value of None.

2. store() - inserts a string into the hashmap; if the bucket or
spot where the string is to be inserted already contains a string,
the string is appended to the bucket. Parameter(s): string.

3. lookup() - 

4. calculate_hash_value() - 

5. get_value() - 
"""


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


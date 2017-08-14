#!/usr/bin/env python


"""
A hash map implementation with one class (HashMap).

The HashMap class consists to five methods:

1. __init__() - creates a list of 10,000 buckets set to a default
value of None.

2. store() - inserts a string into the hashmap; if the bucket or
spot where the string is to be inserted already contains a string,
the string is appended to the bucket. Parameter(s): string.

3. lookup() - returns the hash value of a string if the string is
already in the hash map. If the string is not in the hash map, lookup()
returns -1. Parameter(s): string.

4. calculate_hash_value() - a helper function used to caluculate
a hash value for a string; returns a hash value. Parameter(s): string

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

    def lookup(self, string):
        """Return the hash value if the string is already in the table.
        Return -1 otherwise."""
        # Give the string a hash value
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                # Is the string in the following hv for the table?
                if string in self.table[hash_value]:
                    return hash_value
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a hash value from a string."""
        hash_value = (ord(string[0]) * 100) + ord(string[1])
        return hash_value

    def get_value(self, hash_value):
        """Return the value of a hash."""
        if self.table[hash_value] != None:
            return self.table[hash_value]


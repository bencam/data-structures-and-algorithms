#!/usr/bin/env python


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Returns True if the specified value is in the tree;
        returns False otherwise."""
        return self.preorder_search(self.root, find_val)

    def preorder_search(self, start, find_val):
        """A helper method used to search recursively."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) \
                    or self.preorder_search(start.right, find_val)
        return False


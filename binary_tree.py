#!/usr/bin/env python


"""
A binary tree implementation made up of two classes:

1. Node
Each instance of a node consists of a value (i.e. data), a pointer
to the left node and a pointer to the right node. When an instance
of a node is created, the right and left node pointers are set to
None by default.

2. BinaryTree
Each instance contains a root, which is created by calling the
Node class. In addition to the __init__() method, the BinaryTree
class consists of four methods:

1. search()
2. preorder_search()
3. print_tree()
4. preorder_print()

A simple set of tests follow the Node and BinaryTree classes.
"""


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

    def print_tree(self):
        """Print out all of the tree nodes as each one is visited
        in a pre-order traversal."""
        return self.preorder_print(self.root, "")[:-1]

    def preorder_print(self, start, traversal):
        """A helper method used to recursivelly print tree nodes."""
        if start:
            print start.value
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


# Testing ---
# Create an instance of a binary tree with one node (the root)
# (Note that the BinaryTree class's __init__() method calls the Node
# class, passing in the root as the argument; as a result an instance
# of a binary tree is created along with it's first node.)
tree = BinaryTree('apple')

# Add six nodes to the binary tree instance
tree.root.left = Node('banana')
tree.root.right = Node('babka')
tree.root.left.left = Node('chocolate')
tree.root.left.right = Node('cranberry')
tree.root.right.right = Node('corn')
tree.root.right.left = Node('carrot')

# Call the BinaryTree's search method and search for the 'carrot' node
# (This should return True)
print tree.search('carrot')

# Test the BinaryTree's search method with a node that doesn't exist
# (This should return False)
print tree.search('pancake')

# Test the BinaryTree's print_tree() method
print tree.print_tree()


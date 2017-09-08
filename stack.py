#!/usr/bin/env python


"""
A simple implementation of a stack using a linked list (rather than an
array). The linked list makes it possible for the stack to expand and
shrink as needed (however, extra memory is required as each node needs
a pointer, or next, attribute).
"""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        """Add a node to the end (or tail) of the linked list"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print_ll(self):
        current = self.head
        if current:
            print 'This is the linked list of nodes:'
            while current.next:
                print current.value
                current = current.next
            # Prints the last value in the list
            print current.value
        else:
            print 'This is an empty list.'

    def insert_first(self, new_node):
        """Insert a new node as the first (i.e. the head) node of the
        LinkedList object"""
        new_node.next = self.head
        self.head = new_node

    def delete_first(self):
        """Delete the first (i.e. the head) node in the LinkedList
        and return it"""
        original_head = self.head
        self.head = self.head.next
        return original_head


class Stack(object):

    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def print_stack(self):
        self.ll.print_ll()

    def push(self, new_node):
        """"Push (or add) a new node onto the top of the stack"""
        self.ll.insert_first(new_node)

    def pop(self):
        """"Pop (or remove) the first node off the top of the stack
        and return it"""
        return self.ll.delete_first()


#!/usr/bin/env python


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


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


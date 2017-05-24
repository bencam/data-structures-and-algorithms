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

    def get_node_value(self, position):
        """Return the value of a node at a specified position in the list;
        this method assumes the first position in the list is '1'; it returns
        'None' if the specified position is not in the list or if the list
        is empty"""
        current = self.head
        counter = 1
        if position < 1:
            print '\nYou must choose a position greater than 1.'
            return None
        # Make sure it is not an empty list
        if current:
            # Loop through the nodes
            # Stop if the counter is above the position or if current = None
            while current and counter <= position:
                if counter == position:
                    print '\nHere is the specified node value:'
                    return current.value
                current = current.next
                counter += 1
            print '\nThe specified position is not in this list.'
            return None
        else:
            print '\nThis is an empty list (get_node_value() method).'
            return None


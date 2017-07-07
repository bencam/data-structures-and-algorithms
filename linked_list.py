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
            print 'You must choose a position greater than 1.'
            return None
        # Make sure it is not an empty list
        if current:
            # Loop through the nodes
            # Stop if the counter is above the position or if current = None
            while current and counter <= position:
                if counter == position:
                    print 'Here is the specified node value:'
                    return current.value
                current = current.next
                counter += 1
            print 'The specified position is not in this list.'
            return None
        else:
            print 'This is an empty list (get_node_value() method).'
            return None

    def insert(self, new_node, position):
        """Insert a new node at a specified position; this method
        assumes that the first position in the list is '1'; it
        returns 'None' if the specified position is not in the list
        or if the list is empty; (note that inserting a node as
        position '2' means that the node will be placed between
        nodes '1' and '2'); if the list is empty and the position specified
        is '1', the new_node will be added as the only node in the list"""
        current = self.head
        counter = 1
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_node.next = current.next
                    current.next = new_node
                    print 'New node ' + new_node.value + ' added.'
                current = current.next
                counter += 1
            if counter < position:
                print 'The position specified is out of range of this list.'
        elif position == 1:
            new_node.next = self.head
            self.head = new_node
            print 'New node ' + new_node.value + ' added.'
        elif position < 1:
            print 'To insert a node, a position >= 1 must be selected.'

    def delete(self, value):
        """Delete the first node containing a specified value"""
        current = self.head
        counter = 1
        while current:
            if current.value == value:
                # Check to see if it is the first node in the list
                if counter == 1:
                    self.head = current.next
                # For all other nodes in the list
                else:
                    previous.next = current.next
                print '\nNode ' + value + ' removed.'
            previous = current
            current = current.next
            counter += 1

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


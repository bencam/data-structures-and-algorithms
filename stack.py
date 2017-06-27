#!/usr/bin/env python


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


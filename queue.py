#!/usr/bin/env python


class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        # By passing in 0 as a parameter, we are indicating that the
        # first item in the list should be removed
        return self.storage.pop(0)

    def print_queue(self):
        for item in self.storage:
            print item


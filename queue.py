#!/usr/bin/env python


"""
A simple implementation of a queue with four methods:

1. enqueue - add an element to the end of the queue
2. peek - look at the first element in the queue
3. dequeue - remove and return the first element in the queue (index 0)
4. print_queue - print all of the elements in the queue
"""


class Queue:

    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)

    def print_queue(self):
        for item in self.storage:
            print item


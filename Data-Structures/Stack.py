#!/bin/usr/python3
#Implementing Stack Data Structure

class Stack(object):
    """
    You can visualize Stack data structure as a stack of books placed on top of each other.
    Or even as a stack of plates placed on top of each other.
    """
    def __init__(self):
        self.items = [] #items can be anything like books, plates etc..;

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

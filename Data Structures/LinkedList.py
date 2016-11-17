#!/usr/bin/python3
#implementing linked lists: Singly Linked Lists

from Node import *

# Singly Linked List Implementation
class Singly_Linked_List(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head==None

    def addNode(self, value):
        node = Node(value)
        Next = self.head
        self.head = node
        node.setNext(Next)

    def removeNode(self, value):
        prev = None
        current = self.head
        while current != None:
            if current.getValue() == value:
                prev.setNext(current.getNext())
                break
            prev = current
            current = current.getNext()

    def search(self, value):
        current = self.head
        found = False
        while current != None and not found:
            if current.getValue() == value:
                found = True
            current = current.getNext()
        return found

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count


# WE can also implement the doubly linked list, but before that we have to add a previous pointer to the node class.
#Since it is not much of a challenge . I'm leaving this part out.

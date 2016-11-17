#!/usr/bin/python3
#Implemeting a Node Class

class Node(object):
    def __init__(self, value):
        self.value = value
        self.Next  = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.Next

    def setValue(self, value):
        self.value = value

    def setNext(self, Next):
        self.Next = Next

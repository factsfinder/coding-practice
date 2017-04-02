#!/usr/bin/python3
#Implemeting Dequeue Data Structure

class Dequeue(object):
    """
    Unlike a Queue Data Structure,
    within a Dequeue Data Structure we can add and remove items at
    both front and rear end of the lists..!
    """
    def __init__(self):
        self.people = []

    def isEmpty(self):
        return self.people == []

    def size(self):
        return len(self.people)

    def addFront(self, person):
        self.people.insert(0, person)

    def addRear(self, person):
        self.people.append(person)

    def removeFront(self, person):
        self.people.pop(0)

    def removeRear(self, person):
        self.people.pop()

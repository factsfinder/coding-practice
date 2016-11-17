#!/usr/bin/python3
#Implementing Queue Data Structure

class Queue(object):
    """
    You can visualize a Queue Data Structure as people standing in a queue for tickets.
    #The first person in the queue is always the first to exit the queue.
    """
    def __init__(self):
        self.people = []

    def isEmpty(self):
        return self.people == []

    def enqueue(self, person):
        self.people.append(person)

    def dequeue(self, person):
        self.people.pop(0)

    def size(self):
        return len(self.people)

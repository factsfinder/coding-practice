# Implementation of Binary Tree Data Strucuture

# In a Binary Tree, every parentNode consists only two childs(left_child, right_child) or less.
# The value of left_child is less than parentNode  and the value of right_child is greater than parentNode
# Each Node consists of a value. The Node with no chuldren are called as "Leaf Nodes"
# The top most node is called as "Root Node"
# There are 3 ways to loop or traverse through the nodes
# In-Order Traversal: First left_child, then parentNode and then the right_child
# Pre-Order Traversal: First the parentNode, then left_child and then the right_child
# Post-Order Traversal: First the left_child, then the right_child and then the parentNode

# First we will implement a Node class which we will later make use of in the Binary_Tree class.

# Implementing a Node class
class Node(object):
    # A Constructor method that defines a Node
    def __init__(self, value):
        self.value = value
    # Method to get a value of a Node
    def getValue():
        return self.value
    # Method to set or update a value of a Node
    def setValue(value):
        self.value = value

# Implementing a Binary_Tree class
class Binary_Tree(object):
    def __init__(self):
        self.root = Node(value)
        self.left_child = None
        self.right_child = None
        # Re-initializing the variables without 'self', to avoid typing 'self' again and again. Yes, I'm lazy and We all are :)
        root = self.root
        left_child = self.left_child
        right_child = self.right_child
        parentNode = root

    # Method to add a new node to the tree
    def addNode(value):
        if parentNode.getValue() > value:
            parentNode = left_child
            addNode(value)
            left_child = Node(value)
        if parentNode.getValue() < value:
            parentNode = right_child
            addNode(value)
            right_child = Node(value)

    # Method to determine whether a Node of certain value exists in a tree
    def searchNode(value):
        if parentNode.getValue() == value:
            return True
        if parentNode.getValue() > value:
            parentNode = left_child
            searchNode(value)
        if parentNode.getValue() < value:
            parentNode = right_child
            searchNode(value)
        return False

    # Method to delete a Node
    def deleteNode(value):

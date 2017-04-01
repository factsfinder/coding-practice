# Implementation of Tree and Binary Tree Data Strucuture

# In a Tree, the top most node is called as "Root Node"
# Each Node consists of a value and one or more children nodes. The Node with no children is called as "Leaf Node".

# In a Binary Tree, every parentNode consists two children(left_child, right_child) or less.

# There are 3 ways to loop or traverse through a Binary Tree
# In-Order Traversal: First left_child, then parentNode and then the right_child
# Pre-Order Traversal: First the parentNode, then left_child and then the right_child
# Post-Order Traversal: First the left_child, then the right_child and then the parentNode

class Binary_Tree(object):
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insertLeftChild(self, newNode):
        if self.left_child == None:
            self.left_child = Binary_Tree(newNode)
        else:
            t = Binary_Tree(newNode)
            t.left_child = self.left_child
            self.left_child = t
    def insertRightChild(self, newNode):
        if self.right_child == None:
            self.right_child = Binary_Tree(newNode)
        else:
            t = Binary_Tree(newNode)
            t.right_child = self.right_child
            self.right_child = t

    def inOrder(self):
        if self.root:
            inOrder(self.left_child)
            print(self.root)
            inOrder(self.right_child)
    def preOrder(self):
        if self.root:
            print(self.root)
            inOrder(self.left_child)
            inOrder(self.right_child)
    def postOrder(self):
        if self.root:
            inOrder(self.left_child)
            inOrder(self.right_child)
            print(self.root)

    def getRight(self):
        return self.right_child
    def getLeft(self):
        return self.left_child
    def setRootVal(self, val):
        self.root = val
    def getRootVal(self):
        return self.root

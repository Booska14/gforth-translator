class Node:
    leftChild, rightChild, data = None, None, None

    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data
    def __str__(self):
        return "left child: " + str(self.leftChild) + " right child: " + str(self.rightChild) + " node: " + self.data

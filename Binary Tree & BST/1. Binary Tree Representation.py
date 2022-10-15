class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)
        if self.left is not None:
            self.left.PrintTree()
        if self.right is not None:
            self.right.PrintTree()


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.PrintTree()

'''
             10
       20          30
               40
'''
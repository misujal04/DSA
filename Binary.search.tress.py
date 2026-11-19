#Creating Binary Search Tree

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root == None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if new_node.data < temp.data:
                if temp.left == None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right

    def inorder(self, temp): #self id varible created  for traversing
        if temp == None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data, end= ' ')
            self.inorder(temp.right)

    
    

b1 = BST()
b1.insert(Node(10))
b1.insert(Node(5))
b1.insert(Node(15))
b1.insert(Node(7))
b1.inorder(b1.root)


#!/usr/bin/python3

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        # Value not found in tree
        return False



my_tree = BinarySearchTree()
print(my_tree)

# Test insert method
my_tree.insert(79)
my_tree.insert(80)
my_tree.insert(4)
my_tree.insert(5)
my_tree.insert(10)
my_tree.insert(11)
my_tree.insert(13)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

# Test contains method
print(my_tree.contains(13))
print(my_tree.contains(100))
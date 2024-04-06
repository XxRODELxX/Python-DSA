#!/usr/bin/python3
import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self, value):
        # Creates new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # Add new node at the end of LL
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        # Add new node at the beginning of LL
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def insert(self, index, value):
        # Insert new node at positional location of LL
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def pop(self):
        # Pop (removes) and returns tail/last item of the linked list
        if self.length == 0:
            print("No items/nodes in the Linked List to pop.")
            return None
            
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1 
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def pop_first(self):
        # Pop (removes) and returns head/first item of the linked list
        if self.length == 0:
            print("No items/nodes in the Linked List to pop.")
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value): # set is a Python keyword
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp
         
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# Construct - single item LL
linked_list = LinkedList(4)

# Test append method
linked_list.append(7)
linked_list.append(8)

# Test prepend method
linked_list.prepend(13)

# Test pop_first method
print(linked_list.pop_first())

# Tets print_list method
linked_list.print_list()
#print(linked_list.length)

# Test get method
print("get method: " + str(linked_list.get(1).value))

# Test get method
linked_list.set_value(1, 777)

# Test insert method
linked_list.insert(1, 1)
linked_list.print_list()

# Test remove method
linked_list.remove(1)
linked_list.print_list()

# Test pop method - if currently have 3 items in LL
print(linked_list.pop())
print(linked_list.pop())

# Test edge case when only one item in LL
print(linked_list.pop())

# Test edge case when no items in LL
print(linked_list.pop())

# Test Reverse method
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.print_list()

print("Reverse the Linked List...")

linked_list.reverse()
linked_list.print_list()


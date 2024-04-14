#!/usr/bin/python3

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        temp = self.tail
        if self.head is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail.next = None
            self.tail = temp.prev
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next.prev= None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp
        

# Test Doubly Linked List Constructor
my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.print_list()
print('-------')

# Test append metho1
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(25)
my_doubly_linked_list.print_list()
print('-------')

# Test pop method on 2 or more items
print(my_doubly_linked_list.pop().value)
print(my_doubly_linked_list.pop().value)
# Test pop method on 1 or more items
print(my_doubly_linked_list.pop().value)
# Test pop method on 0 or more items
print(my_doubly_linked_list.pop())

# Test prepend method with zero nodes current
print('-------')
my_doubly_linked_list.prepend(3)
my_doubly_linked_list.prepend(2)
my_doubly_linked_list.prepend(1)
my_doubly_linked_list.print_list()
print('-------')

# Test pop_first method - 3 items
print(my_doubly_linked_list.pop_first().value)
print("current list:")
my_doubly_linked_list.print_list()
print('-------')

# Test pop_first method - 1 items
print(my_doubly_linked_list.pop_first().value)
print(my_doubly_linked_list.pop_first().value)
print("current list:")
my_doubly_linked_list.print_list()
print('-------')

# Test pop_first method - 0 items
print(my_doubly_linked_list.pop_first())
print("current list:")
my_doubly_linked_list.print_list()
print('-------')

# Test get method
my_doubly_linked_list.append(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

print(my_doubly_linked_list.get(1).value)
print(my_doubly_linked_list.get(3).value)
print('-------')

# Test set method
my_doubly_linked_list.set_value(3, 33)
my_doubly_linked_list.print_list()
print('-------')

# Test insert method
my_doubly_linked_list.insert(2, 777)
my_doubly_linked_list.print_list()
print('-------')

# Test remove method
print(my_doubly_linked_list.remove(2).value, '\n')
my_doubly_linked_list.print_list()
#!/usr/bin/python3

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        hash_idx = self.__hash(key)
        if self.data_map[hash_idx] == None:
            self.data_map[hash_idx] = []
        self.data_map[hash_idx].append([key, value])

    def get_item(self, key):
        hash_idx = self.__hash(key)
        if self.data_map[hash_idx] != None:
            check = [ x[1] for x in self.data_map[hash_idx] if x[0] == key ]
            if check:
                return check[0]
        return None

    def keys(self):
        all_keys = []
        for i in self.data_map:
            if i != None:
                keys = [x[0] for x in i]
                all_keys = all_keys + keys
        return all_keys

    def print_table(self):
        for key, val in enumerate(self.data_map):
            print(key, ": ", val) 

my_hash_table = HashTable()
my_hash_table.print_table()

# Test set_item method
my_hash_table.set_item('ribs', 77)
my_hash_table.set_item('brisket', 33)
my_hash_table.set_item('chicken', 120)
my_hash_table.set_item('wings', 120)
my_hash_table.set_item('lagers', 523)
my_hash_table.set_item('ipa', 470)
my_hash_table.print_table()

# Test get_item method
print(my_hash_table.get_item('ipa'))
print(my_hash_table.get_item('beer'))

# Test keys method
print(my_hash_table.keys())



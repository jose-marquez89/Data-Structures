from singly_linked_list.singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying
   storage structure. Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""

"""
Using arrays
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        count = 0
        for i in self.storage:
            count += 1
        return count

    def push(self, value):
        new = self.storage.append(value)
        return new

    def pop(self):
        if len(self.storage) != 0:
            out = self.storage.pop()
            return out
        else:
            return None
"""


class Stack:
    # uses linked lists
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size != 0:
            out = self.storage.remove_tail()
            self.size -= 1
            return out
        else:
            return None

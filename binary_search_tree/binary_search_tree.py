from .kyoo import Queue
from .stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if value is more or less
        # than this node
        if value >= self.value:
            # if value is more than or equal, direct to the right
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        elif value < self.value:
            # if value is less than or equal to, direct to left
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if self.value is target
        if self.value != target:
            # send the search in the correct direction
            if self.right and target > self.value:
                target_exists = self.right.contains(target)
                if target_exists:
                    return True
            elif self.left and target < self.value:
                target_exists = self.left.contains(target)
                if target_exists:
                    return True
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        most = self.value
        if self.right:
            nxt = self.right.get_max()
            if nxt > most:
                return nxt
        else:
            return most

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)
        else:
            return

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)

        while len(q) > 0:
            node = q.dequeue()
            print(node.value)

            # enqueue left node
            if node.left:
                q.enqueue(node.left)

            if node.right:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while len(stack) > 0:
            node = stack.pop()
            print(node.value)

            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


if __name__ == "__main__":
    bst = BSTNode(1)
    numbers = [8, 5, 7, 6, 3, 4, 2]
    for n in numbers:
        bst.insert(n)
    bst.in_order_print(bst)
    print()
    bst.bft_print(bst)

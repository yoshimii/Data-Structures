import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
  
        
    # Insert the given value into the tree
    def insert(self, value):             
        if self.value is None:
            self.value = value
            
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else: self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else: self.right.insert(value)
        else:
            pass
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else: 
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()
            
        
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
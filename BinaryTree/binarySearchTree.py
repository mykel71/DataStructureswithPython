# 
"""
    A Binary Search Tree
    
    Example:
                8
               / \
              3   10
            /  \     \
           1    6     14
               / \   /
              4   7 13
              
    >>> t = BinarySearchTree()
    >>> t.insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
    >>> print(" ".join(repr(i.value) for i in t.traversal_tree()))
    8 3 1 6 4 7 10 14 13
    >>> print(" ".join(repr(i.value) for i in t.traversal_tree(postorder)))
    1 4 7 6 3 13 14 10 8
    >>> t.remove(20)
    Traceback (most recent call last):
        ...
    ValueError: Value 20 not found
    >>> BinarySearchTree().search(6)
    Traceback (most recent call last):
        ...
    IndexError: Warning: Tree is empty! please use another.
    
    Other example:
    
    >>> testlist = (8, 3, 6, 1, 10, 14, 13, 4, 7)
    >>> t = BinarySearchTree()
    >>> for i in testlist:
    ...     t.insert(i)
    
    Prints * the elements of the list in order traversal
    >>> print(t)
    {'8': ({'3': (1, {'6': (4, 7)})}, {'10: (None, {'14': (13, None)})})}
    
    Test existence
    >>> t.search(6) is not None
    True
    >>> t.search(-1) is not None
    False
    
    >>> t.search(6).is_right
    True
    >>> t.search(1).is_right
    False
    
    >>> t.get_max().value
    14
    >>> t.get_min().value
    1
    >>> t.empty()
    False
    >>> for i in testlist:
    ...     t.remove(i)
    >>> t.empty()
    True
"""

from collections.abc import Iterable
from typing import Any

class Node:
    def __init__(self, value: int | None = None):
        self.value = value
        self.parent: Node | None = None # added in order to delete a node easier
        self.left: Node | None = None
        self.right: Node | None = None
        
    def __repr__(self) -> str:
        from pprint import pformat
        
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)
    
    @property
    def is_right(self) -> bool:
        return self.parent is not None and self is self.parent.right
    

class BinarySearchTree:
    def __init__(self, root: Node | None = None):
        self.root = root
        
    def __str__(self) -> str:
        # Return a string of all the Nodes using in order traversal
        return str(self.root)
        
    def __reassgn_nodes(self, node: Node, new_children: Node | Node) -> None:
        if new_children is not None: # reset its kids
            new_children.parent = node.parent
        if node.parent is not None: #reset its parent
            if node.is_right: # if it is the right child
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children
        
    def empty(self) -> bool:
        return self.root is None
    
    
            
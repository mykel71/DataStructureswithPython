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


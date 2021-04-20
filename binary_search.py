from bisect import bisect_left, bisect_right
import unittest
import random
import numpy as np

def binaryLeftSearch(arr: list, target: int) -> int:
    """Binary Search in sorted array, returning
    the left most index where the element can be inserted
    if the target is not in the array.

    :param arr: Sorted list to search in
    :type arr: list
    :param target: Target to search for
    :type target: int
    :return: Return index at which to insert target or the
    index of target if it exists
    :rtype: int
    """

    l = 0
    h = len(arr)

    while l < h:
        m = (l + h) // 2
        if arr[m] < target:
            l = m + 1
        else:
            h = m
    
    return h

def binaryRightSearch(arr: list, target: int) -> int:
    """Binary Search in sorted array, returning
    the right most index where the element can be inserted
    if the target is not in the array.

    :param arr: Sorted list to search in
    :type arr: list
    :param target: Target to search for
    :type target: int
    :return: Return index at which to insert target or the
    index of target if it exists
    :rtype: int
    """

    l = 0
    h = len(arr)

    while l < h:
        m = (l+h) // 2
        if arr[m] > target:
            h = m
        else:
            l = m + 1
    
    return l

class TreeNode:

    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> list:

        traversal = []

        def inorder_traversal(node: 'TreeNode') -> None:

            if node is None:
                return

            inorder_traversal(node.left)
            traversal.append(node.val)
            inorder_traversal(node.right)
        
        inorder_traversal(self)
        return str(traversal)

class TestSearch(unittest.TestCase):

    def test_select_left(self):
        arr = sorted(list(np.random.randint(0, 100, size=(10))))
        target = random.choice(arr)

        print(arr)
        print(target)

        self.assertEqual(binaryLeftSearch(arr, target), bisect_left(arr, target))

    
    def test_select_right(self):
        arr = sorted(list(np.random.randint(0, 100, size=(10))))
        target = random.choice(arr)

        print(arr)
        print(target)

        self.assertEqual(binaryRightSearch(arr, target), bisect_right(arr, target))

unittest.main()

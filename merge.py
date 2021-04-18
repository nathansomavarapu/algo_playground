import unittest
import random
import numpy as np

def merge(arr1: list, arr2: list) -> list:
    """Merge two lists which are each sorted.

    :param arr1: Sorted list
    :type arr1: list
    :param arr2: Sorted list
    :type arr2: list
    :return: Merge of arr1 and arr2 in sorted order
    :rtype: list
    """

    p1 = p2 = 0
    n = len(arr1)
    m = len(arr2)

    merged_arr = []

    while p1 < n and p2 < m:

        v1 = arr1[p1]
        v2 = arr2[p2]

        if v1 < v2:
            merged_arr.append(v1)
            p1 += 1
        if v2 < v1:
            merged_arr.append(v2)
            p2 += 1
        if v1 == v2:
            merged_arr.append(v1)
            merged_arr.append(v2)
            p1 += 1
            p2 += 1
    
    while p1 < n:
        v1 = arr1[p1]
        merged_arr.append(v1)
        p1 += 1
    
    while p2 < m:
        v2 = arr2[p2]
        merged_arr.append(v2)
        p2 += 1
    
    return merged_arr

def merge_sort(arr1: list) -> list:
    """Apply the merge routine to recursively
    merge sort an array.

    :param arr1: Array to be sorted
    :type arr1: list
    :return: Sorted array
    :rtype: list
    """
    
    if len(arr1) == 1:
        return arr1
    
    l = 0
    h = len(arr1)
    m = (l + h) // 2

    left_arr = merge_sort(arr1[:m])
    right_arr = merge_sort(arr1[m:])

    return merge(left_arr, right_arr)

class TestSelection(unittest.TestCase):

    def test_merge(self):
        arr1 = sorted(list(np.random.randint(0, 100, size=(10))))
        arr2 = sorted(list(np.random.randint(0, 100, size=(15))))

        merged_arr = merge(arr1, arr2)

        self.assertEqual(merged_arr, sorted(arr1 + arr2))
    
    def test_mergesort(self):
        arr1 = list(np.random.randint(0, 100, size=(103)))

        ms_array = merge_sort(arr1)

        self.assertEqual(ms_array, sorted(arr1))

unittest.main()
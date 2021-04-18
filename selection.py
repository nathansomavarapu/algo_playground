import random
import unittest
import numpy as np

def swap(arr: list, i: int, j: int):
    """Swap elements i and j by reference

    :param arr: array to swap
    :type arr: list
    :param i: first swap index
    :type i: int
    :param j: second swap index
    :type j: int
    """
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def kSelect(arr: list, k: int) -> int:
    """Return the k-th element from the array if it were sorted.

    :param arr: Array of numbers
    :type arr: list
    :param k: Element index to return the value at
    :type k: int
    :param selection_strategy: Pivot selection strategy, defaults to 'random'
    :type selection_strategy: str, optional
    :return: Value at index k
    :rtype: int
    """

    if len(arr) == 1 and k == 0:
        return arr[0]

    n = len(arr)
    pivot_idx = random.randint(0,n-1)
    pivot = arr[pivot_idx]

    tmp = arr[-1]
    arr[-1] = pivot
    arr[pivot_idx] = tmp
    
    pivot_idx = n-1

    store = 0
    for i,val in enumerate(arr):
        if val < pivot:
            swap(arr, store, i)
            store += 1
    
    swap(arr, pivot_idx, store)

    if store < k:
        sub_arr = arr[store+1:]
        return kSelect(sub_arr, k - len(arr[:store+1]))
    elif store > k:
        return kSelect(arr[:store], k)
    else:
        return arr[store]

def quicksort(arr: list, left: int, right: int) -> list:
    """Take in a list and sorts it using quicksort. The pivots are chosen
    randomly each time. The algorithm runs in place.

    :param arr: Array to be sorted
    :type arr: list
    :param left: left index to sort from
    :type left: int
    :param right: right index to sort to
    :type right: int
    :return: sorted array
    :rtype: list
    """

class TestSelection(unittest.TestCase):

    def test_select(self):
        arr = list(np.random.randint(0, 25, size=(10)))
        k = random.randint(0, len(arr)-1)

        selected = kSelect(arr, k)
        sorted_choose = sorted(arr)[k]

        print(arr)
        print(sorted_choose)
        print(selected)

        self.assertEqual(selected, sorted_choose)

unittest.main()
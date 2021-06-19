import random
import unittest
import numpy as np

from typing import Tuple, List

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

def partition(arr: list, pivot_idx: int) -> Tuple[list, int]:
    n = len(arr)
    pivot = arr[pivot_idx]

    swap(arr, pivot_idx, n-1)

    pivot_idx = n-1

    store = 0
    for i,val in enumerate(arr):
        if val < pivot:
            swap(arr, store, i)
            store += 1
    
    swap(arr, pivot_idx, store)

    return arr, store


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

    # if len(arr) == 1 and k == 0:
    #     return arr[0]

    n = len(arr)
    pivot_idx = random.randint(0,n-1)

    partitioned_arr, pivot_index = partition(arr, pivot_idx)

    if pivot_index < k:
        sub_arr = partitioned_arr[pivot_index+1:]
        return kSelect(sub_arr, k - len(partitioned_arr[:pivot_index+1]))
    elif pivot_index > k:
        return kSelect(partitioned_arr[:pivot_index], k)
    else:
        return arr[pivot_index]

def select_iterative(arr: List[int], k: int) -> int:
    left = 0
    right = len(arr)

    while True:

        pivot_idx = random.randint(left, right-1)
        pivot = arr[pivot_idx]
        arr[right-1], arr[pivot_idx] = arr[pivot_idx], arr[right-1]
        pivot_idx = right-1

        free = left
        for i in range(left, right):
            v = arr[i]
            if v < pivot:
                arr[i], arr[free] = arr[free], arr[i]
                free += 1
        
        arr[pivot_idx], arr[free] = arr[free], arr[pivot_idx]

        if k == free:
            return arr[free]
        if k > free:
            left = free + 1
        if k < free:
            right = free    

def quicksort(arr: list) -> list:
    """Take in a list and sorts it using quicksort. The pivots are chosen
    randomly each time. The algorithm runs in place.

    :param arr: Array to be sorted
    :type arr: list
    :return: sorted array
    :rtype: list
    """

    if len(arr) == 1 or len(arr) == 0:
        return arr

    n = len(arr)
    pivot_idx = random.randint(0,n-1)

    parr, pind = partition(arr, pivot_idx)

    left = quicksort(parr[:pind])
    right = quicksort(parr[pind+1:])

    return left + [parr[pind]] + right


class TestSelection(unittest.TestCase):

    def test_select(self):
        arr = list(np.random.randint(0, 25, size=(10)))
        k = random.randint(0, len(arr)-1)

        selected = kSelect(arr, k)
        sorted_choose = sorted(arr)[k]

        self.assertEqual(selected, sorted_choose)
    
    def test_quicksort(self):
        arr = list(np.random.randint(0, 25, size=(10)))

        self.assertEqual(quicksort(arr), sorted(arr))

# unittest.main()

arr = [41,2,3,6,12,5,10]
s_arr = sorted(arr)
true_val = s_arr[5]
for _ in range(10000):
    select_val = select_iterative(arr, 5)
    assert select_val == true_val
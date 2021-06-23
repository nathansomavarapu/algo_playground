from typing import List, Union

import random
import unittest

class FenwickTree:

    def __init__(self, arr: List[int]):
        self.arr = arr[:]
        self.ftree_arr = self._construct_tree(arr)
    
    def _construct_tree(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr = [0] + arr

        prefix_sum = []
        for v in arr:
            if len(prefix_sum) != 0:
                prefix_sum.append(prefix_sum[-1] + v)
            else:
                prefix_sum.append(v)
        
        ftree = [0] * (n+1)
        for idx in range(1, n+1):
            ftree[idx] = prefix_sum[idx] - prefix_sum[idx-self._lowest_one_bit(idx)]
        
        return ftree
    
    def _sum(self, idx: int) -> int:
        acc = 0
        while idx > 0:
            acc += self.ftree_arr[idx]
            idx -= self._lowest_one_bit(idx)
        return acc

    def range_sum(self, left: int, right: int) -> int:
        """Returns the range sum for values between left and right
        inclusive on the left endpoint. Equivalent to sum(arr[left, right]).

        :param left: Index to start sum at
        :type left: int
        :param right: Index to end sum at
        :type right: int
        :return: sum(arr[left:right])
        :rtype: int
        """
        if left >= right:
            return 0
        
        left_sum = self._sum(left)
        right_sum = self._sum(right)
        return right_sum - left_sum

    def update(self, idx: int, delta: int) -> None:
        n = len(self.arr)
        orig_idx = idx
        idx += 1

        while idx <= n:
            self.ftree_arr[idx] += delta
            idx += self._lowest_one_bit(idx)
        
        self.arr[orig_idx] += delta

    def _lowest_one_bit(self, idx: int) -> int:
        idx_tc = ~idx + 1
        return idx & idx_tc
    
    def __getitem__(self, idx: int) -> Union[int, List[int]]:
        return self.arr[idx]
    
    def __setitem__(self, idx: int, val: int) -> None:
        delta = val - self.arr[idx]
        self.update(idx, delta)
    
    def __len__(self) -> int:
        return len(self.arr)

class TestFTree(unittest.TestCase):        

    def test_range_sum(self):
        n = 1000
        arr = [random.randint(-1000, 1000) for _ in range(n)]
        ftree = FenwickTree(arr)
        
        for i in range(n):
            for j in range(i, n):
                self.assertEqual(ftree.range_sum(i,j), sum(arr[i:j]))
    
    def test_get_item(self):
        n = 1000
        arr = [random.randint(-1000, 1000) for _ in range(n)]
        ftree = FenwickTree(arr)
        self.assertEqual(len(ftree), n)

        for i in range(len(arr)):
            self.assertEqual(ftree[i], arr[i])
    
    def test_update(self):
        n = 100
        arr = [random.randint(-1000, 1000) for _ in range(n)]
        ftree = FenwickTree(arr)

        for i in range(len(arr)):
            v = random.randint(-10,10)

            prev = ftree[i]
            ftree.update(i, v)
            self.assertEqual(ftree[i], prev+v)
            arr[i] += v

            for i in range(n):
                for j in range(i, n):
                    self.assertEqual(ftree.range_sum(i,j), sum(arr[i:j]))
    
    def test_set_item(self):
        n = 100
        arr = [random.randint(-1000, 1000) for _ in range(n)]
        ftree = FenwickTree(arr)
        
        for i in range(n):
            v = random.randint(-100,100)

            ftree[i] = v
            self.assertEqual(ftree[i], v)
            arr[i] = v

            for i in range(n):
                for j in range(i, n):
                    self.assertEqual(ftree.range_sum(i,j), sum(arr[i:j]))
        

unittest.main()
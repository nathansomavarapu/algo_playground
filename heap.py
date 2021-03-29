from typing import List
from random import shuffle

class Heap:

    def __init__(self, data=[]):
        self.data = []
        if len(data) > 0:
            self.heapify(data)

    def heapify(self, data: List):
        for val in data:
            self.add(val)

    def add(self, data: int):
        self.data.append(data)
        idx = len(self.data) - 1
        parent_val, parent_idx = self.parent(idx)

        while parent_val is not None and parent_val > self.data[idx]:
            tmp = self.data[parent_idx]
            self.data[parent_idx] = self.data[idx]
            self.data[idx] = tmp
            
            idx = parent_idx
            parent_val, parent_idx = self.parent(idx)
    
    def parent(self, idx):
        parent_idx = int((idx - 1) / 2)
        parent = None
        if parent_idx >= 0:
            parent = self.data[parent_idx]
        
        return parent, parent_idx
    
    def left(self, idx):
        left_idx = 2 * idx + 1
        left = None
        if left_idx < len(self.data):
            left = self.data[left_idx]
        return left, left_idx
    
    def right(self, idx):
        right_idx = 2 * (idx + 1)
        right = None
        if right_idx < len(self.data):
            right = self.data[right_idx]
        return right, right_idx

    def peak(self):
        return self.data[0]

    def pop(self):
        val = self.data[0]
        tmp_root = self.data.pop(-1)
        self.data[0] = tmp_root

        import pdb; pdb.set_trace()

        if len(self.data) > 1:
            idx = 0

            left_val, left_idx = self.left(idx)
            right_val, right_idx = self.right(idx)

            while True:
                import pdb; pdb.set_trace()
                if left_val is None and right_val is None:
                    break
                    
                if left_val is None:
                    if right_val < self.data[idx]:
                        tmp = self.data[right_idx]
                        self.data[right_idx] = self.data[idx]
                        self.data[idx] = tmp
                    else:
                        break
                
                if right_val is None:
                    if left_val < self.data[idx]:
                        tmp = self.data[left_idx]
                        self.data[left_idx] = self.data[idx]
                        self.data[idx] = tmp
                    else:
                        break

                if self.data[idx] <= left_val and self.data[idx] <= right_val:
                    break

                min_dir = None

                if left_val < right_val and left_val < self.data[idx]:
                    min_dir = 'left'
                if right_val < left_val and right_val < self.data[idx]:
                    min_dir = 'right'

                if min_dir == 'left':
                    tmp = left_val
                    self.data[left_idx] = self.data[idx]
                    self.data[idx] = tmp

                    idx = left_idx
                elif min_dir == 'right':
                    tmp = right_val
                    self.data[right_idx] = self.data[idx]
                    self.data[idx] = tmp

                    idx = right_idx
                left_val, left_idx = self.left(idx)
                right_val, right_idx = self.right(idx)

        return val

    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return self.data.__str__()


def main():
    test_arr = list(range(10))
    shuffle(test_arr)

    print(test_arr)
    min_heap = Heap(test_arr)
    print(min_heap)

    print(min_heap.pop())

if __name__ == '__main__':
    main()
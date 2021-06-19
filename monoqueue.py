from operator import eq, le, ge
from typing import Callable

class MStack:
    
    def __init__(self, comparison: Callable):
        self.op = comparison
        self.ordered_st = []
        self.base_st = []

    def enqueue(self, item: int) -> None:
        if len(self.ordered_st) == 0 or self.op(item, self.ordered_st[-1]):
            self.ordered_st.append(item)
        self.base_st.append(item)

    def getTop(self) -> int:
        return self.ordered_q[-1]

    def deque(self) -> int:
        curr = self.base_st.pop()
        if curr == self.ordered_st[-1]:
            self.ordered_st.pop()
        return curr
    
    def __len__(self) -> int:
        return len(self.base_st)

    def __repr__(self) -> str:
        return 'Stack: {}\nMStack: {}'.format(str(self.base_st), str(self.ordered_st))

class MinMStack(MStack):
    
    def __init__(self):
        super().__init__(le)
    
    def getMin(self) -> int:
        return self.getTop()

class MaxMStack(MStack):

    def __init__(self):
        super().__init__(ge)
    
    def getMax(self) -> int:
        return self.getTop()

maxs = MinMStack()
a = [1,4,2,8,3,32,12,32,98]
for v in a:
    maxs.enqueue(v)
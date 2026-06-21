from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.cur_summ = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.cur_summ -= self.q.popleft()
        self.cur_summ += val
        self.q.append(val)  
        return self.cur_summ/float(len(self.q))      


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

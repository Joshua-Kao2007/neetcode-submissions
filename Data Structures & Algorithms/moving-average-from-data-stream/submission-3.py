from collections import deque
# do this with a circular queue

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.q = [0]*size
        self.length = 0
        self.front = 0
        self.rear = 0
        self.cur_summ = 0

    def next(self, val: int) -> float:
        if self.length == self.size:
            self.cur_summ -= self.q[self.front]
            self.front = (self.front+1)%self.size
            self.length -= 1

        self.cur_summ += val
        self.q[self.rear] = val 
        self.rear = (self.rear+1)%self.size
        self.length += 1

        return self.cur_summ/float(self.length)      


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

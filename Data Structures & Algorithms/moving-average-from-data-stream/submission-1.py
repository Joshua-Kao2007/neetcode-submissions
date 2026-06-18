class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.cur_num = 0
        # circular buffer?
    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.cur_num -= self.q.popleft()
        self.q.append(val)
        self.cur_num += val
        return self.cur_num / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

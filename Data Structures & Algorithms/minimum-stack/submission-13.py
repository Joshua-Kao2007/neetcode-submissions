class MinStack:

    def __init__(self):
        self.stack = []
        self.localMins = []
        
    def push(self, val:int) -> None:
        self.stack.append(val)
        if not self.localMins or val <= self.localMins[-1]:
            self.localMins.append(val)
            
    def pop(self) -> None:
        x = self.stack.pop()
        if self.localMins and x == self.localMins[-1]:
            self.localMins.pop()
        
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        
    def getMin(self) -> int:
        return self.localMins[-1] if self.localMins else None
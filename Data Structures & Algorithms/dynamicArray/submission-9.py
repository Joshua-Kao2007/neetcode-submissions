class DynamicArray:
    
    def __init__(self, capacity: int):
        self.elements = 0
        self.capacity = capacity
        self.data = [None]*self.capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.elements:
            raise IndexError("Index out of bounds")
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.elements:
            raise IndexError("out of bounds")
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.elements >= self.capacity:
            self.resize()
        self.data[self.elements] = n
        self.elements += 1

    def popback(self) -> int:
        if self.elements == 0:
            raise IndexError("can't popback")
        tmp = self.data[self.elements-1]
        self.data[self.elements-1] = None
        self.elements -= 1
        return tmp

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_data = [None]*new_capacity
        for i in range(self.elements):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.elements
    
    def getCapacity(self) -> int:
        return self.capacity

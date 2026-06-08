class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None]*capacity
        self.elements = 0

    def get(self, i: int) -> int:
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.elements:
            self.resize()
        self.data[self.elements] = n
        self.elements += 1

    def popback(self) -> int:
        cur_element = self.data[self.elements-1]
        self.data[self.elements-1] = None
        self.elements -= 1
        return cur_element

    def resize(self) -> None:
        new_capacity = 2* self.capacity
        new_data = [None]*new_capacity
        for i in range(self.capacity):
            new_data[i] = self.data[i]
        self.capacity = new_capacity
        self.data = new_data

    def getSize(self) -> int:
        return self.elements
    
    def getCapacity(self) -> int:
        return self.capacity
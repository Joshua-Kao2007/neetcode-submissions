class TreeMap:
    
    def __init__(self):
        # One for key value pair is hashmap
        # getMin and GetMax and getInorderKeys()
        self.hashing = {}

    def insert(self, key: int, val: int) -> None:
        self.hashing[key] = val

    def get(self, key: int) -> int:
        return self.hashing.get(key, -1)

    def getMin(self) -> int:    
        min_val = float('inf')
        best_val = -1
        for k,v in self.hashing.items():
            if k < min_val:
                min_val = k
                best_val = v
        return best_val

    def getMax(self) -> int:
        max_val = float('-inf')
        best_val = -1
        for k,v in self.hashing.items():
            if k > max_val:
                max_val = k
                best_val = v
        return best_val

    def remove(self, key: int) -> None:
        if key in self.hashing:
            del self.hashing[key]

    def getInorderKeys(self) -> List[int]:
        li = []
        for k,v in self.hashing.items():
            li.append(k)
        return sorted(li)

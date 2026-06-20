class StringIterator:
    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.cur_letter = self.compressedString[0] # guranteed to be a letter
        self.pointer = 1
        self.cur_remaining = 0
        while self.pointer < len(self.compressedString) and self.compressedString[self.pointer].isdigit():
            self.cur_remaining = (self.cur_remaining*10) + int(self.compressedString[self.pointer])
            self.pointer += 1

    def next(self) -> str:
        if not self.hasNext():
            return " "
        if self.cur_remaining == 0:
            self.cur_letter = self.compressedString[self.pointer]
            self.pointer += 1
            while self.pointer < len(self.compressedString) and self.compressedString[self.pointer].isdigit():
                self.cur_remaining = (self.cur_remaining*10) + int(self.compressedString[self.pointer])
                self.pointer += 1
        
        if self.cur_remaining > 0:
            self.cur_remaining -= 1
            return self.cur_letter
        return " "

    def hasNext(self) -> bool:
        # if another letter then return True, else return False
        if self.cur_remaining == 0 and self.pointer >= len(self.compressedString):
            return False
        return True
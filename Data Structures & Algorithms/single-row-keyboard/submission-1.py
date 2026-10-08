class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mappings = {}
        for i in range(len(keyboard)):
            mappings[keyboard[i]] = i
        summ = 0
        cur_let = 0
        for let in word:
            summ += abs(cur_let-mappings[let])
            cur_let = mappings[let]
        return summ

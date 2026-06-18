class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mapping = {}
        for idx,num in enumerate(keyboard):
            mapping[num] = idx
        cnt = 0
        last_letter = 0
        for letter in word:
            x = mapping[letter]
            cnt +=  abs(x-last_letter)
            last_letter = x
        return cnt
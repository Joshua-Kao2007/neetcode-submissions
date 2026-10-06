class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        for i in range(len(x)-1, -1, -1):
            if x[i] != "":
                return len(x[i])

        return 0
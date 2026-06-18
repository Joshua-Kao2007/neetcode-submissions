class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = Counter(s)
        ones = 0
        for k,v in freq.items():
            if v % 2 != 0:
                ones += 1
        return True if ones <= 1 else False

        # #abba

        # # cdldc
        # if even: same frequency everywhere
        # if odd: same frequency except for like one letter
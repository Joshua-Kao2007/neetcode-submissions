from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        bad = 0
        for cnt,freq in count.items():
            if freq%2 != 0:
                bad += 1
        return True if bad <= 1 else False
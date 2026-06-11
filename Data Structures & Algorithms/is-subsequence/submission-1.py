class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == len(t): return s==t

        # Brute Force
        cur_letter = 0
        for letter in t:
            if cur_letter < len(s) and letter == s[cur_letter]:
                cur_letter += 1
        
        return cur_letter == len(s)



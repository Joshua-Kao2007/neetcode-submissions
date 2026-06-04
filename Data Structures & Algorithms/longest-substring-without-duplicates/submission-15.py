class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Edge Cases: Length 0 or length 1: just return legnth of string s
        LENGTH = len(s)
        if LENGTH <= 1: return LENGTH

        # Initalize Variables
        best = 0
        L = 0
        used = set()
        for R in range(LENGTH):
            while s[R] in used:
                used.remove(s[L])
                L += 1
            used.add(s[R])
            best = max(best, R-L+1)

        return best

        # Length of longest subsutring without duplicate characters
        # must be contiguous substring?
        # abcdeff --> 6 because at the seventh character we dupliate the f

        # Use a hashmap or a set some data structure to store current characters in the substring
        # once we get to a character in the set, remove characters until that character is not in the set, decreasing count/window accordingly. then continue iterating to the end of the length of the string
        # Linear O(N) Time, O(N) extra space
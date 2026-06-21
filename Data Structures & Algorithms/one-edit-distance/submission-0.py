class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        L,R = 0,0
        if len(s) == len(t):
            # They must only replaceexactly one character
            strikes = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    strikes += 1
            return strikes == 1
        elif len(s)+1 == len(t):
            # you must insert exactly one character into s
            strikes = 0
            for i in range(len(t)):
                if L == len(s) or t[i] != s[L]:
                    strikes += 1
                else:
                    L += 1
            return strikes == 1
        elif len(s)-1 == len(t):
            # you must delete exactly one character from s
            strikes = 0
            for i in range(len(s)):
                if R == len(t) or s[i] != t[R]:
                    strikes += 1
                else:
                    R += 1
            return strikes == 1
        else:
            return False


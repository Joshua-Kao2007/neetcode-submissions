class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        pointerS, pointerT = 0, 0

        while pointerS < len(s) and pointerT < len(t):
            if s[pointerS] == t[pointerT]:
                pointerS += 1
            pointerT += 1
        return True if pointerS == len(s) else False
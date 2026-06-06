class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        cache = {}
        def helper(L:int, R:int, cache:dict[tuple(int),int])->int:
            if L == len(text1) or R == len(text2): return 0
            if (L,R) in cache:
                return cache[(L,R)]
            if text1[L] == text2[R]:
                cache[(L,R)] = 1 + helper(L+1,R+1, cache)
            else:
                cache[(L,R)] = max(helper(L+1,R, cache), helper(L,R+1,cache))
            return cache[(L,R)]
        return helper(0,0, cache)
        
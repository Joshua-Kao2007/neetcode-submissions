class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
 
        chars_have = 0
        chars_need = 0

        actualCountS = {}
        CountT = {}

        # Step 1: Initalize countS dictionaries and CountT freq for t string
        for let in t:
            if let not in CountT:
                CountT[let] = 1
                actualCountS[let] = 0
                chars_need += 1
            else:
                CountT[let] += 1

        min_len, min_best, L = float('inf'), "", 0

        for R in range(len(s)):
            actualCountS[s[R]] = actualCountS.get(s[R], 0)+1
            if s[R] in CountT and actualCountS[s[R]] == CountT[s[R]]:
                chars_have += 1
            
            while chars_have == chars_need:
                if R-L+1 < min_len: #uninclusive of the R index...
                    min_len = R-L+1
                    min_best = s[L:R+1]

                actualCountS[s[L]] -= 1
                if s[L] in CountT and actualCountS[s[L]] < CountT[s[L]]:
                    chars_have -= 1
            
                L += 1
            
        return min_best



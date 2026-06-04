from collections import Counter, defaultdict
class Solution:
    def check(self, countT, countS)->bool:
        for k,v in countT.items():
            if k not in countS: return False
            if countS[k] < countT[k]: return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        lengthS, lengthT = len(s), len(t)
        if lengthT > lengthS: return ""
        countT = Counter(t)
        countS = {}
        bestL,bestR, min_seq,L = -1,-1, float('inf'),0
        for R in range(lengthS):
            if s[R] not in countS:
                countS[s[R]] = 0
            countS[s[R]] += 1
            while self.check(countT, countS):
                if R-L+1 < min_seq:
                    bestL,bestR = L,R
                    min_seq = R-L+1
                countS[s[L]]-=1
                L += 1
        return s[bestL:bestR+1] 
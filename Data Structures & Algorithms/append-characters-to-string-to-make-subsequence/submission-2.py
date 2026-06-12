class Solution:
    def findLongest(self, s:str,t:str)->int:
        if t=="": return 0
        i,j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return j

    def appendCharacters(self, s: str, t: str) -> int:
        longest = self.findLongest(s,t)
        return len(t) - longest
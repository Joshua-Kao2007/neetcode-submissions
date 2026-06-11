class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        s_chr = [0]*26
        t_chr = [0]*26
        for char in s:
            s_chr[ord(char)-ord('a')] += 1
        for char in t:
            t_chr[ord(char)-ord('a')] += 1
        return s_chr == t_chr
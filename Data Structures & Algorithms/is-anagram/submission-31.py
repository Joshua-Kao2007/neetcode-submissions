from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = defaultdict(int), defaultdict(int)
        for letter in s:
            dict_s[letter] += 1
        for letter in t:
            dict_t[letter] += 1
        return dict_s == dict_t

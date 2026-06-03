from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Sorting Method. 
        # res = defaultdict(list)
        # for string in strs:
        #     s = "".join(sorted(string))
        #     res[s].append(string)
        # return list(res.values())

        # 2. Character Method
        x = [0]*26
        res = defaultdict(list)
        for string in strs:
            for let in string:
                x[ord(let)-ord('a')]+=1
            res[tuple(x)].append(string)
            x = [0]*26
        return list(res.values())
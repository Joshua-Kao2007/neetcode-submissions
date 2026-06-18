class Solution:
    def findDiff(self, word):
        # wrapping around functaionlity
        # a:0, z:26
        # b:0, a:1
        # a y -2
        # a x -3
        # a w -4
        diff = []
        for let in range(0, len(word)-1):
            y = ord(word[let+1])
            x = ord(word[let])
            if y >= x:
                diff.append(y-x) #25
            else: # convert to positive 
                diff.append(26-(x-y)) #25
        return tuple(diff)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # abc --> Bcd " are they equivalent"
        res = defaultdict(list)
        for string in strings:
            x = self.findDiff(string)
            res[x].append(string)
        return list(res.values())
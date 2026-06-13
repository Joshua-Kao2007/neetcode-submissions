class Solution:
    def createMapping(self, words):
        res = defaultdict(list)
        for w1,w2 in words: # if not distinct it'd chanage
            res[w1].append(w2)
            res[w2].append(w1)
        return res
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # 1. Same length
        if len(sentence1) != len(sentence2): return False
        res = self.createMapping(similarPairs)
        # 2. Check similarity
        for i in range(len(sentence1)):
            if sentence2[i] != sentence1[i] and sentence2[i] not in res[sentence1[i]]:
                return False
        return True


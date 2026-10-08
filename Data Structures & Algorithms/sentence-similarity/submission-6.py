class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        mapping = defaultdict(set)
        for word1,word2 in similarPairs:
            mapping[word1].add(word2)
            mapping[word2].add(word1)
        
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if sentence2[i] not in mapping[sentence1[i]]:
                return False
        return True
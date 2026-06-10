class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # Edge Case
        if word1 == word2: return 0

        # Initialize
        lastOccurence1 = -1
        lastOccurence2 = -1
        LENGTH = len(wordsDict)
        min_dist = float('inf')

        # Core Algorithm
        for i in range(LENGTH):
            cur_word = wordsDict[i]
            if cur_word == word1:
                if lastOccurence2 != -1:
                    min_dist = min(abs(i - lastOccurence2), min_dist)
                lastOccurence1 = i
            elif cur_word == word2:
                if lastOccurence1 != -1:
                    min_dist = min(abs(i - lastOccurence1), min_dist)
                lastOccurence2 = i
        return min_dist




    # # Input: List[str]. word1: str, word2 str. Word1 and Word2 exist in wordsDict. 
    # - Case-sensitive? Lowercase
    # - Sorted lexographically? Totally random string. 
    # - Dupliactes. Yes. KEY CONSTRAINT. Duplicates. ****
    # - 

    # # Output. Integer. Shoretest distance between these two words in the list. 
    # - Shortest distance mean here? 
    # - practice: (0, 5)
    # - coding: (3, 6) --> 1. absolute value shortest dsitance between the two words. 
    
    # # Edge Cases:
    # - Word1 and word2 going to be the same? If they are the same. Return 0
    # - Duplicates. ADDITIONAL ALGORITHM that finds the minimum difference between all the occurences of word1 and word2 in wordsDict. 

    # # Data Structures:
    # - last occurence of word1
    # - last occurrence of word2
    # - **DUPLICATES

    # # Core Algorithm:
    # - Iterate One Pass Thru wordsDict
    # - Flag when word1 (index) shows up. Flag when word2 (index) shows up. 
    # - If there were no duplicates and word1 and word2 are gurantted to exist:
    #     - abs(word2-word1)
    # - are duplicates:
    #     - 

    # wordsDict = ["coding", "abc", "practice", "ddd", "ggg", "practice", "coding"]
    # last_occurnce_coding = 6
    # last_occurence_practice = 5
    # MIN_VALUE = 2. 2 < 5 --> 2. 1 < 2. 1. 

    # - Variable keeping track of the last occurnce of the other word. Updating each word accordingly when a new occurnce shows up. 








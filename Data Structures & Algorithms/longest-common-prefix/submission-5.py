class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {} # allows us to check lookup in O(1) Time
        self.isEnd = False
    
class Solution:
    def findShortestWord(self, strs):
        best_cnt = float('inf')
        for word in strs:
            x = len(word)
            if x < best_cnt:
                best_cnt = x
        return best_cnt

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Step 1: Add each word into the Trie letter by letter
        dummy = TrieNode(-1)
        for word in strs:
            cur_node = dummy
            for let in word:
                if let in cur_node.children:
                    cur_node = cur_node.children[let]
                    continue
                new_node = TrieNode(let)
                cur_node.children[let] = new_node
                cur_node = new_node
            cur_node.isEnd = True
        
        # Step 2: Iterate thru the Trie
        cur_node = dummy
        res = []
        cur_cnt = 0
        best_cnt = self.findShortestWord(strs)
        while cur_node.children:
            if len(cur_node.children) == 1 and cur_cnt < best_cnt:
                res.append(next(iter(cur_node.children)))
            else:
                break
            cur_node = next(iter(cur_node.children.values()))
            cur_cnt += 1
        return "".join(res)

        # Use a trie to go step by step downwards till there's more than one divergences
        #     b
        #   a
        # t g k n
        # --> Therefore there is just 1 divergence...
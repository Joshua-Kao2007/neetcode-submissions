class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {} # allows us to check lookup in O(1) Time
        self.isEnd = False
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Step 1: Add each word into the Trie letter by letter
        dummy = TrieNode(-1)
        for word in strs:
            cur_node = dummy
            for let in word:
                found = False
                for val in cur_node.children.keys():
                    if let == val:
                        cur_node.children[let] = (cur_node.children[let][0], cur_node.children[let][1]+1)
                        cur_node = cur_node.children[let][0]
                        found = True
                        break
                if not found:
                    new_node = TrieNode(let)
                    cur_node.children[let] = (new_node, 1)
                    cur_node = new_node
        # Step 2: Iterate thru the Trie
        cur_node = dummy
        res = []
        while cur_node.children:
            if len(cur_node.children) == 1 and next(iter(cur_node.children.values()))[1] == len(strs):
                res.append(next(iter(cur_node.children)))
                cur_node = cur_node.children[next(iter(cur_node.children))][0]
            else:
                break
        return "".join(res)
        # Use a trie to go step by step downwards till there's more than one divergences
        #     b
        #   a
        # t g k n
        # --> Therefore there is just 1 divergence...
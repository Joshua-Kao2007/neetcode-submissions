class TrieNode:
    def __init__(self, val):
        self.children = {} # allows us to check lookup in O(1) Time
        self.val = val
    
class Trie:
    def __init__(self):
        self.root = TrieNode(-1)
    
    def add_node(self, word):
        cur_node = self.root
        for let in word:
            if let not in cur_node.children:
                cur_node.children[let] = TrieNode(let)
            cur_node = cur_node.children[let]
    def lcp(self, length):
        cur_cnt = 0
        cur_node = self.root
        res = []
        while cur_cnt < length:
            if len(cur_node.children) == 1:
                cur_cnt += 1
                res.append(next(iter(cur_node.children.keys())))
            else:
                break
            cur_node = next(iter(cur_node.children.values()))
        return "".join(res)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_trie = Trie()
        for word in strs:
            new_trie.add_node(word)
        shortest = min(len(s) for s in strs)
        return new_trie.lcp(shortest)
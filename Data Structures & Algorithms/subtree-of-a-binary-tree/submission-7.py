# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        x = deque([root])
        while x:
            LENGTH = len(x)
            for _ in range(LENGTH):
                a = x.popleft()
                if self.isSameTree(a, subRoot):return True
                if a.left: x.append(a.left)
                if a.right: x.append(a.right)
        return False

    def isSameTree(self, root: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root and not root2: return True
        if not root or not root2: return False
        if root.val != root2.val: return False
        return self.isSameTree(root.left, root2.left) and self.isSameTree(root.right, root2.right)
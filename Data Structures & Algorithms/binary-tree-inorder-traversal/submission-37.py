# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, li):
        if not root:
            return li
        self.helper(root.left, li)
        li.append(root.val)
        self.helper(root.right, li)
        return li

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.helper(root, [])
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValueNode(self, root):
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # 0 or 1 children
            if not root.left or not root.right:
                return root.left if root.left else root.right
            successor = self.minValueNode(root.right)
            successor.left = root.left
            return root.right
        return root

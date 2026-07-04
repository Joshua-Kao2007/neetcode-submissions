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
        parent = None
        cur = root
        while cur and cur.val != key:
            parent = cur
            if cur.val > key:
                cur = cur.left
            else:
                cur = cur.right      
        if not cur: #doesn't exist
            return root

        # 0 or 1 children
        child = None
        if not cur.right or not cur.left:
            child = cur.right if cur.right else cur.left
            if not parent:
                return child
            if parent.val > cur.val:
                parent.left = child
            else:
                parent.right = child
            return root

        # 2 children
        successor = self.minValueNode(cur.right)
        successor.left = cur.left
        if not parent:
            return root.right
        if parent.val > cur.val:
            parent.left = successor
        else:
            parent.right = successor

        return root       
        

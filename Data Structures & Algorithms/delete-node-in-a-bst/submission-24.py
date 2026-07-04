# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
        successor_parent = cur
        successor = cur.right
        while successor.left:
            successor_parent = successor
            successor = successor.left
        
        if successor_parent != cur:
            successor_parent.left = successor.right
            successor.right = cur.right

        successor.left = cur.left
        if not parent:
            return successor
        
        if parent.left == cur:
            parent.left = successor
        else:
            parent.right = successor
        
        return root



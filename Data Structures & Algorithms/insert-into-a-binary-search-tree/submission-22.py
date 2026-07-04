# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        # Iteratively
        parent = TreeNode(-1)
        parent.left = root
        cur = root
        while True:
            if not cur:
                if parent.val < val:
                    parent.right = TreeNode(val)
                else:
                    parent.left = TreeNode(val) 
                return root

            parent = cur
            if cur.val > val:
                cur = cur.left
            elif cur.val < val:
                cur = cur.right

        return root
        
        
        # # Recursive
        # if not root:
        #     return TreeNode(val)
        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left, val)
        # elif root.val < val:
        #     root.right = self.insertIntoBST(root.right, val)
        # return root
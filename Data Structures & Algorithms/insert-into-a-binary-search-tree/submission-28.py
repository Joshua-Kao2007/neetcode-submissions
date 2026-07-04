# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # No parent
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            if cur.val > val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
            elif cur.val < val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right

        return root
        
        # if not root:
        #     return TreeNode(val)
        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left, val)
        # elif root.val < val:
        #     root.right = self.insertIntoBST(root.right, val)
        # return root
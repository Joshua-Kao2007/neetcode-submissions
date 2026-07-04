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

        parent = None
        cur = root

        while cur:
            parent = cur
            if cur.val > val:
                cur = cur.left
            elif cur.val < val:
                cur = cur.right
            else:
                return
        
        # we've found where ccur needs to be replaced
        if parent.val < val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)

        return root
        
        # if not root:
        #     return TreeNode(val)
        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left, val)
        # elif root.val < val:
        #     root.right = self.insertIntoBST(root.right, val)
        # return root
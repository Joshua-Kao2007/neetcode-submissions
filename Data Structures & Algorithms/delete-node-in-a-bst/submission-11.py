# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValueNode(self, root: Optional[TreeNode])->int:
        if not root:return
        while root and root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # delete if found
        # when deleting it can have 0/1 children or it can have 2 children
        if not root: return None

        if root.val < key: 
            root.right = self.deleteNode(root.right, key)

        elif root.val > key: 
            root.left = self.deleteNode(root.left, key)

        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            successor = self.minValueNode(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

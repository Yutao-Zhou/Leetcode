# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(root):
            if root:
                flat(root.left)
                flat(root.right)
                tmp = root.right
                root.right = root.left
                root.left = None
                n = root
                while n.right:
                    n = n.right
                n.right = tmp
        flat(root)
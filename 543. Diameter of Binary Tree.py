# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #### Recursive return max deepth ####
        def recursion(node):
            if not node:
                return 0
            l = recursion(node.left)
            r = recursion(node.right)
            self.ans = max(self.ans, l + r)
            return max(l, r) + 1
        self.ans = 0
        recursion(root)
        return self.ans
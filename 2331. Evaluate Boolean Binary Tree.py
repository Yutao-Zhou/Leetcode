# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        #### Recursion ####
        def recursion(node):
            if node:
                if node.val == 0 or node.val == 1:
                    return node.val
                if node.val == 2:
                    return recursion(node.left) or recursion(node.right)
                if node.val == 3:
                    return recursion(node.left) and recursion(node.right)
        return recursion(root) 
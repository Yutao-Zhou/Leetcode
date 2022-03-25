# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #### DFS store sum ####
        if not root:
            return False
        s = root.val
        stack = [(root, s)]
        while stack:
            current = stack.pop()
            node = current[0]
            s = current[1]
            if node:
                if node.left:
                    stack.append((node.left, s + node.left.val))
                if node.right:
                    stack.append((node.right, s + node.right.val))
                if node.left == None and node.right == None and s == targetSum:
                    return True
        return False
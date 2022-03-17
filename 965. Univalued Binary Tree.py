# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        #### DFS ####
        stack = []
        check = root.val
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if node.val != check:
                    return False
                else:
                    stack.append(node.right)
                    stack.append(node.left)
        return True
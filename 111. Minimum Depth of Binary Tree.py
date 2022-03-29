# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #### DFS ####
        if not root:
            return 0
        ans = float("inf")
        deep = 1
        stack = [(root, 1)]
        while stack:
            node = stack.pop()
            current = node[0]
            if current:
                deep = node[1]
                if current.left:
                    stack.append((current.left, deep + 1))
                if current.right:
                    stack.append((current.right, deep + 1))
                if not current.left and not current.right:
                    ans = min(ans, deep)
        return ans
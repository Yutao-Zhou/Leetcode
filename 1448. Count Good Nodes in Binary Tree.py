# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #### DFS pass max ####
        ans = 1
        stack = [(root, root.val)]
        while stack:
            node = stack.pop()
            current = node[0]
            maximum = node[1]
            if current:
                if current.left:
                    if current.left.val >= maximum:
                        ans += 1
                    stack.append((current.left, max(maximum, current.left.val)))
                if current.right:
                    if current.right.val >= maximum:
                        ans += 1
                    stack.append((current.right, max(maximum, current.right.val)))
        return ans
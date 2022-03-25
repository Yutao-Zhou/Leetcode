# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        #### DFS store sum ####
        if not root:
            return []
        ans = []
        path = [root.val]
        stack = [(root, path)]
        while stack:
            current = stack.pop()
            node = current[0]
            path = current[1]
            if node:
                if node.left:
                    stack.append((node.left, path + [node.left.val]))
                if node.right:
                    stack.append((node.right, path + [node.right.val]))
                if node.left == None and node.right == None and sum(path) == targetSum:
                    ans.append(path)
        return ans
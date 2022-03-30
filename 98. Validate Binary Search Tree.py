# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #### DFS check while ####
        # def check(node, lower, upper):
        #     if not node:
        #         return True
        #     if lower < node.val < upper:
        #         return check(node.left, lower, node.val) and check(node.right, node.val, upper)
        #     else:
        #         return False
        # return check( node = root, lower = float("-inf"), upper = float("inf") )
        
        #### inorder recursive ####
        def inorder(root, path):
            if root:
                inorder(root.left, path)
                path.append(root.val)
                inorder(root.right, path)
                return path
        path = []
        inorder(root, path)
        for i in range(1, len(path)):
            if path[i] <= path[i - 1]:
                return False
        return True
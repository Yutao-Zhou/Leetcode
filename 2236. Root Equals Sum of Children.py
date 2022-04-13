# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        #### No thinking ####
        # return root.left.val + root.right.val == root.val
        
        #### recursive ####
        ans = []
        def recursive(root):
            if root:
                recursive(root.left)
                recursive(root.right)
                ans.append(root.val)
        recursive(root)
        return ans[0] + ans[1] == ans[2]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #### Binary search ####
        # while 1:
        #     if p.val < root.val and q.val < root.val:
        #         root = root.left
        #     if p.val > root.val and q.val > root.val:
        #         root = root.right
        #     if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
        #         return root
        #     if p == root or q == root:
        #         return root
        
        #### Simpler search ####
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
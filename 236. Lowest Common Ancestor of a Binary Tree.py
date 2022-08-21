# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #### Recursive ####
        def find(node):
            if not node:
                return
            if node.val == p.val or node.val == q.val:
                return node
            l, r = find(node.left), find(node.right)
            if l and r:
                if (l.val == p.val and r.val == q.val) or (l.val == q.val and r.val == p.val):
                    return node
            if not l or not r:
                return r or l
        return find(root)
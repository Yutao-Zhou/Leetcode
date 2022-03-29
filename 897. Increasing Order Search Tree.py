# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        #### inorder recursive and build ####
        def inorder(root):
            if root:
                inorder(root.left)
                path.append(root.val)
                inorder(root.right)
                return path
        path = []
        inorder(root)
        path = path[::-1]
        ans = None
        for i in path:
            cache = TreeNode(i, None, None)
            cache.right = ans
            ans = cache
        return ans
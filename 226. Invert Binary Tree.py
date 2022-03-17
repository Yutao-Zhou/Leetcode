# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #### BFS ####
        # que = []
        # cache = root
        # que.append(root)
        # while que:
        #     node = que.pop(0)
        #     if node:
        #         cache = node.left
        #         node.left = node.right
        #         node.right = cache
        #         que.append(node.left)
        #         que.append(node.right)
        # return root
        
        #### invert ####
        if root:
            invert = self.invertTree
            root.left, root.right = invert(root.right), invert(root.left)
        return root
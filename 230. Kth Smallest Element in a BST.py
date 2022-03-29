	# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #### DFS ordinary ####
        # path = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         path.append(node.val)
        #         if node.left:
        #             stack.append(node.left)
        #         if node.right:
        #             stack.append(node.right)
        # path = sorted(path)
        # return path[k - 1]
        
        #### inorder recursive ####
        def pathInorder(root):
            if root:
                pathInorder(root.left)
                path.append(root.val)
                pathInorder(root.right)
                return path
        path = []
        pathInorder(root)
        return path[k - 1]
        
        #### inorder iterative ####
        # stack = []
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return root.val
        #     root = root.right
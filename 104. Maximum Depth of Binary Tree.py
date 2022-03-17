# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #### BFS modified ####
#         from collections import deque
        
#         if not root:
#             return 0
#         que = deque([root])
#         num_node_level = 1
#         levels = 0
#         while que:
#             node = que.popleft()
#             if node.left:
#                 que.append(node.left)
#             if node.right:
#                 que.append(node.right)
#             num_node_level -= 1
#             if num_node_level == 0:
#                 levels += 1
#                 num_node_level = len(que)
                
#         return levels
        #### recursive ####
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
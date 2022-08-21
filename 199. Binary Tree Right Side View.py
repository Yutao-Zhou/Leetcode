# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #### BFS Level tranversal ####
#         if not root: # corner case
#             return []
        
#         currentLevel, currentRight, lastNode, ans = 0, 0, None, []
#         queue = deque([(root, 0)])
        
#         while queue:
#             node = queue.popleft()
#             if node[0]:
#                 if node[1] > currentLevel:
#                     ans.append(lastNode.val)
#                     currentLevel = node[1]
#                 lastNode = node[0]
#                 queue.append((node[0].left, node[1] + 1))
#                 queue.append((node[0].right, node[1] + 1))
        
#         ans.append(lastNode.val)
#         return ans

        #### DFS Recursive ####
        def recurse(node, deepth):
            if node:
                if deepth == len(ans):
                    ans.append(node.val)
                recurse(node.right, deepth + 1)
                recurse(node.left, deepth + 1)
            
        ans = []
        recurse(root, 0)
        return ans
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        #### DFS Iteritive ####
        # ans, stack = 0, [(root, 1)]
        # while stack:
        #     node = stack.pop()
        #     if node[0]:
        #         ans = max(ans, node[1])
        #         for c in node[0].children:
        #             stack.append((c, node[1] + 1))
        # return ans
        
        #### recursive ####
        def recursion(node):
            if not node:
                return 0
            if not node.children:
                return 1
            return max(recursion(c) for c in node.children) + 1
        return recursion(root)
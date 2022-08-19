"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #### DFS Iteritive ####
        # ans, stack = [], [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         ans.append(node.val)
        #         for i in range(len(node.children) - 1, -1, -1):
        #             stack.append(node.children[i])
        # return ans
        
        #### DFS Recursive ####
        # def preorder(node):
        #     if node:
        #         ans.append(node.val)
        #         for n in node.children:
        #             preorder(n)
        # ans = []
        # preorder(root)
        # return ans
        
        #### Local Variable ####
        ans = []
        if root:
            ans.append(root.val)
            for n in root.children:
                ans.extend(self.preorder(n))
        return ans
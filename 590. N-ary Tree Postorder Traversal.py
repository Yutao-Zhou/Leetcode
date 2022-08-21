"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        #### Recursive ####
        # def postOrder(node):
        #     if node:                    
        #         for c in node.children:
        #             postOrder(c)
        #         ans.append(node.val)
        # ans = []
        # postOrder(root)
        # return ans
        
        #### Local Variable ####
        # ans = []
        # if root:
        #     for n in root.children:
        #         ans.extend(self.postorder(n))
        #     ans.append(root.val)
        # return ans
        
        #### Iteritive ####
        ans, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.extend(node.children)
        return ans[::-1]
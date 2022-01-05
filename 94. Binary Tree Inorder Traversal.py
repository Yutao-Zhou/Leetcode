# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #### recursion ####
        # ans = []
        # if root == None:
        #     return ans
        # ans += self.inorderTraversal(root.left)
        # ans.append(root.val)
        # ans += self.inorderTraversal(root.right)
        # return ans
    
        #### Iterative Traversal ####
        ans = []
        stack = []
        while 1:
            while root:
                stack.append(root)
                root = root.left
            if stack == []:
                return ans
            node = stack.pop()
            ans.append(node.val)
            root = node.right
        
        #### stack flag ####
        # ans = []
        # stack = [(root,False)]
        # while stack:
        #     node,flage = stack.pop()
        #     if node:
        #         if flage == False:
        #             stack.append((node.right,False))
        #             stack.append((node,True))
        #             stack.append((node.left,False))
        #         else:
        #             ans.append(node.val)
        # return ans
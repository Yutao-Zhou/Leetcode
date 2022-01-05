# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #### recursion ####
        # ans = []
        # if root == None:
        #     return ans
        # ans += self.postorderTraversal(root.left)
        # ans += self.postorderTraversal(root.right)
        # ans.append(root.val)
        # return ans
    
        #### Iterative traversal reverse ####
        # ans = []
        # if root == None:
        #     return ans
        # stack = [root]
        # while stack:
        #     topNode = stack.pop()
        #     ans.append(topNode.val)
        #     if topNode.left != None:
        #         stack.append(topNode.left)
        #     if topNode.right != None:
        #         stack.append(topNode.right)
        # return ans[::-1]
        
        #### visit tag ####
        ans = []
        stack = [(root,False)]
        while stack:
            node, visited = stack.pop()
            if node != None:
                if visited == True:
                    ans.append(node.val)
                else:
                    stack.append((node,True))
                    stack.append((node.right,False))
                    stack.append((node.left,False))
        return ans
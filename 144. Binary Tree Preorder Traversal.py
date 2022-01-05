# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #### recursion ####
        # ans = []
        # if root == None:
        #     return ans
        # ans.append(root.val)
        # print("first",ans)
        # ans += self.preorderTraversal(root.left)
        # print("second",ans)
        # ans += self.preorderTraversal(root.right)
        # print("third",ans)
        # return ans
        
        #### Iterative Traversal ####
        ans = []
        if root == None:
            return ans
        stack = [root]
        while stack:
            topNode = stack.pop()
            print("first",ans,stack)
            ans.append(topNode.val)
            print("second",ans,stack)
            if topNode.right != None:
                stack.append(topNode.right)
                print("third",ans,stack)
            if topNode.left != None:
                stack.append(topNode.left)
                print("fourth",ans,stack)
        return ans
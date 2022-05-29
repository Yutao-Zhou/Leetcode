# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #### dfs ####
        # def allLeaf(root):
        #     ans = []
        #     que = [root]
        #     while que:
        #         node = que.pop()
        #         if node:
        #             if node.left:
        #                 que.append(node.left)
        #             if node.right:
        #                 que.append(node.right)
        #             if not node.left and not node.right:
        #                 ans.append(node.val)
        #     return ans
        # sequence1 = allLeaf(root1)
        # sequence2 = allLeaf(root2)
        # return sequence1 == sequence2
        
        #### inorder append ####
        def recursive(root):
            if not root.left and not root.right:
                ans.append(root.val)
            if root.left:
                recursive(root.left)
            if root.right:
                recursive(root.right)
        ans = []
        recursive(root1)
        sequence1 = ans
        ans = []
        recursive(root2)
        sequence2 = ans
        return sequence1 == sequence2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        #### Recursive ####
        def subTree(node, subtreeSum, subtreeNumber):
            if not node:
                return 0, 0
            lsubSum, lsubNum = subTree(node.left, subtreeSum, subtreeNumber)
            rsubSum, rsubNum = subTree(node.right, subtreeSum, subtreeNumber)
            if node.val == (lsubSum + rsubSum + node.val) // (lsubNum + rsubNum + 1):
                self.ans += 1
            return lsubSum + rsubSum + node.val, lsubNum + rsubNum + 1
        self.ans = 0
        subTree(root, root.val, 1)
        return self.ans
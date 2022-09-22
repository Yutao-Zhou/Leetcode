# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode(0)]
        ans = []
        for i in range(1, n - 1):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - 1 - i)
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans
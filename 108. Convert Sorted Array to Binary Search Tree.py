# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def DAC(l, r):
            mid = (l + r) // 2
            if l > r:
                return None
            root = TreeNode(nums[mid])
            root.left = DAC(l, mid - 1)
            root.right = DAC(mid + 1, r)
            return root
        return DAC(0, len(nums) - 1)
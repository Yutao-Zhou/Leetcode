# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        #### devide and conquer ####
        # def DAC(nums):
        #     if not nums:
        #         return None
        #     m = nums.index(max(nums))
        #     root = TreeNode(nums[m])
        #     root.left = DAC(nums[0 : m])
        #     root.right = DAC(nums[m + 1 : len(nums)])
        #     return root
        # return DAC(nums)
        
        #### stack ####
        stack = []
        for x in nums:
            n = TreeNode(x)
            while stack and x > stack[-1].val:
                n.left = stack.pop()
            if stack:
                stack[-1].right = n               
            stack.append(n)
        return stack[0]
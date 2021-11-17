class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        for j in range(1,len(nums)):
            for i in range(0,j):
                if nums[i] < nums[j] and nums[j] - nums[i] > ans:
                    ans = nums[j] - nums[i]
        return ans
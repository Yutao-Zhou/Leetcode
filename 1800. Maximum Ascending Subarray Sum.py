class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        #### keep max subarray sum with variable ####
        ans = nums[0]
        cache = nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= nums[i - 1]:
                cache = nums[i]
            if nums[i] > nums[i - 1]:
                cache += nums[i]
            if cache > ans:
                ans = cache
        return ans
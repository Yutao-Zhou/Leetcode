class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #### DP bottm up ####
        # LIS = [1] * len(nums)
        # for i in range(len(nums) - 1, -1, -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])
        # return max(LIS)
        
        #### DP top down ####
        LIS = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and LIS[j] + 1 > LIS[i]:
                    LIS[i] = LIS[j] + 1
        return max(LIS)
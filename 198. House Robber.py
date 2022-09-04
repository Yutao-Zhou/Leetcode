class Solution:
    def rob(self, nums: List[int]) -> int:
        #### DP ####
        # n = len(nums)
        # memo = [0] * n
        # for i in range(n):
        #     if i < 2:
        #         memo[i] = nums[i]
        #     else:
        #         memo[i] = max(memo[:i - 1]) + nums[i]
        # return max(memo)
        
        #### DP Space Optimization ####
        n = len(nums)
        if n <= 2:
            return max(nums)
        maxBefore = nums[0]
        last = nums[1]
        for i in range(2, n):
            tmp = last
            last = maxBefore + nums[i]
            maxBefore = max(maxBefore, tmp)
        return max(last, maxBefore)
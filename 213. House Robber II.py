class Solution:
    def rob(self, nums: List[int]) -> int:
        #### DP ####
        # def rob(nums):
        #     n = len(nums)
        #     memo = [0] * n
        #     for i in range(n):
        #         if i < 2:
        #             memo[i] = nums[i]
        #         else:
        #             memo[i] = max(memo[:i - 1]) + nums[i]
        #     return max(memo)
        # if len(nums) == 1:
        #     return nums[0]
        # return max(rob(nums[:-1]), rob(nums[1:]))
        
        #### DP Space Optimization ####
        def rob(nums):
            if n <= 2:
                return max(nums)
            maxBefore = nums[0]
            last = nums[1]
            for i in range(2, n):
                tmp = last
                last = maxBefore + nums[i]
                maxBefore = max(maxBefore, tmp)
            return max(last, maxBefore)
        n = len(nums)
        if n == 1:
            return nums[0]
        n -= 1
        return max(rob(nums[1:]), rob(nums[:-1]))
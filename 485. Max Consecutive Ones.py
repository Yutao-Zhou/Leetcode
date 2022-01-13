class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #### one pass two constant variable ####
        # ans = 0
        # cache = 0
        # for i in nums:
        #     if i == 0:
        #         cache = 0
        #     if i == 1:
        #         cache += 1
        #     if cache > ans:
        #         ans = cache
        # return ans
        
        #### string ####
        ans = 0
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        nums = "".join(nums)
        nums = nums.split("0")
        for i in nums:
            if len(i) > ans:
                ans = len(i)
        return ans
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #### separate and recreat ####
        # positive = []
        # negative = []
        # ans = []
        # for n in nums:
        #     if n > 0:
        #         positive.append(n)
        #     if n < 0:
        #         negative.append(n)
        # for i in range(len(positive)):
        #     ans.append(positive[i])
        #     ans.append(negative[i])
        # return ans
        
        #### two pointer ####
        i = 0
        j = 0
        ans = []
        while i < len(nums) and j < len(nums):
            if nums[i] < 0:
                i += 1
            if nums[j] > 0:
                j += 1
            if nums[i] > 0 and nums[j] < 0:
                ans.append(nums[i])
                ans.append(nums[j])
                i += 1
                j += 1
        return ans
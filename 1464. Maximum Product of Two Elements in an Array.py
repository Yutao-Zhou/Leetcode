class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #### brute force ####
        # ans = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] - 1) * (nums[j] - 1) > ans:
        #             ans = (nums[i] - 1) * (nums[j] - 1)
        # return ans
        
        #### sort ####
        # nums = sorted(nums)
        # return (nums[-1] - 1) * (nums[-2] - 1)
        
        #### find top two numbers ####
        a, b = 0, 0
        for i in nums:
            if i >= a:
                b = a
                a = i
            elif i > b:
                b = i
        return (a - 1) * (b - 1)
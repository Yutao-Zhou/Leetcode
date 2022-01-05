class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #### math ####
        # ans = 0
        # check = min(nums)
        # for i in nums:
        #     ans += i - check
        # return ans
        
        #### formula ####
        # return sum(nums) - min(nums) * len(nums)
        
        #### really doing it the hard way ####
        ans = 0
        while 1:
            nums.sort()
            if len(set(nums)) == 1:
                return ans
            else:
                for i in range(len(nums) - 1):
                    nums[i] += 1
                ans += 1
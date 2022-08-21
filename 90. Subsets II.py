class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #### Backtract Brute Force ####
        # def Backtract(start, current):
        #     if len(current) == k:
        #         if current not in ans:
        #             ans.append(current)
        #         return
        #     for i in range(start, l):
        #         Backtract(i + 1, current + [nums[i]])
        # ans, l = [], len(nums)
        # nums.sort()
        # for k in range(l + 1):
        #     Backtract(0, [])
        # return ans
        
        #### Backtract skip each start ####
        # def Backtract(start, current):
        #     if len(current) == k:
        #         ans.append(current)
        #         return
        #     for i in range(start, l):
        #         if i !=  start and nums[i] == nums[i - 1]:
        #             continue
        #         Backtract(i + 1, current + [nums[i]])
        # ans, l = [], len(nums)
        # nums.sort()
        # for k in range(l + 1):
        #     Backtract(0, [])
        # return ans
        
        #### Iteritive little by little ####
        ans = [[]]
        nums.sort()
        for n in nums:
            cache = []
            for c in ans:
                nc = c + [n]
                if nc not in ans:
                    cache.append(nc)
            ans = ans + cache
        return ans
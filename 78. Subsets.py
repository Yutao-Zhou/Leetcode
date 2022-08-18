class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #### Backtrack ####
        # def backtrack(start, current):
        #     if len(current) == k:
        #         ans.append(current)
        #         return
        #     else:
        #         for i in range(start, l):
        #             backtrack(i + 1, current + [nums[i]])
        # ans, l = [], len(nums)
        # for k in range(l + 1):
        #     backtrack(0, [])
        # return ans
        
        #### Iteritive ####
        # result = [[]]
        # for n in nums:
        #     for i in range(len(result)):
        #         result.append(result[i] + [n])
        # return result
        
        #### DFS ####
        def dfs(nums, current):
            ans.append(current)
            for i in range(len(nums)):
                dfs(nums[i + 1:], current + [nums[i]])
        ans = []
        dfs(nums, [])
        return ans
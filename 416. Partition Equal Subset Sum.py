class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #### Backtrack ####
        # def put(i, remain):
        #     if remain == 0:
        #         return True
        #     elif remain < 0 or (i == len(nums) and remain != 0):
        #         return False
        #     elif put(i + 1, remain) or put(i + 1, remain - nums[i]):
        #         return True
        
        # if sum(nums) % 2:
        #     return False
        # return put(0, sum(nums) // 2)

        #### DP Topdown ####
        def put(i, remain):
            if memo[remain - 1][i] != None:
                return memo[remain - 1][i]
            if remain == 0:
                memo[remain - 1][i] = True 
                return True
            elif remain < 0 or (i == len(nums) and remain != 0):
                memo[remain - 1][i] = False
                return False
            result = put(i + 1, remain) | put(i + 1, remain - nums[i])
            memo[remain - 1][i] = result
            return result
        
        if sum(nums) % 2:
            return False
        memo = [[None for i in range(len(nums) + 1)] for j in range(sum(nums) // 2 + 1)]
        return put(0, sum(nums) // 2)
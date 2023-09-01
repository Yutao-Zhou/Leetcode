class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        #### Sort ####
        ans = 0
        for row in nums:
            row.sort()
        for i in range(len(nums[0])):
            score = 0
            for row in nums:
                score = max(score, row[i])
            ans += score
        return ans
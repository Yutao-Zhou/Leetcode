class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        #### Bottom up DP ####
        memo = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)):
            memo[i][i] = nums[i]
        for x in range(1, len(nums)):
            for y in range(0, len(nums) - x):
                memo[y][x + y] = max(nums[x + y] - memo[y][x + y - 1], nums[y] - memo[y + 1][x + y])
        return memo[0][-1] >= 0
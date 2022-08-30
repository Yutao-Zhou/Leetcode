class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        #### DP ####
        def rotate(i):
            DP[i] = DP[i - 1] + s - n * nums[n - i]
        n = len(nums)
        s = sum(nums)
        DP = [0] * n
        for i in range(1, n):
            DP[0] += i * nums[i]
        for i in range(1, n):
            rotate(i)
        return max(DP)
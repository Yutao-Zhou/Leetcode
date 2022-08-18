class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        #### DP ####
        l = len(arr)
        DP = [0] * l
        for j in range(l):
            maxK = 0
            for i in range(j, max(-1, j - k), -1):
                maxK = max(maxK, max(arr[i : j + 1]) * (j - i + 1) + DP [i - 1])
            DP[j] = maxK
        return DP[-1]
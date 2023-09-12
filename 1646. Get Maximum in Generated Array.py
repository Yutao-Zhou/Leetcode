class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        #### DP bottomup ####
        if n == 0:
            return 0
        memo = [0] * (n + 1)
        memo[1] = 1

        for x in range(2, n + 1):
            if x % 2:
                memo[x] = memo[(x - 1) // 2] + memo[1 + (x - 1) // 2]
            else:
                memo[x] = memo[x // 2]

        return max(memo)
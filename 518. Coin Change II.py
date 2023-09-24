class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #### DP Bottomup ####
        dp = [[-1 for i in range(amount + 1)] for j in range(len(coins) + 1)]
        dp[0] = [0] * (amount + 1)
        for i in range(len(dp)):
            dp[i][0] = 1

        for y in range(1, len(dp)):
            for x in range(1, len(dp[0])):
                dp[y][x] = dp[y - 1][x]
                if x - coins[y - 1] >= 0:
                    dp[y][x] += dp[y][x - coins[y - 1]]
        return dp[-1][-1]
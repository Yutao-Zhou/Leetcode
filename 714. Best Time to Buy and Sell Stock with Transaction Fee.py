class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #### DP ####
        # n = len(prices)
        # memo = [[0,1] for i in range(n)]
        # memo[0][1] = -prices[0]
        # for i in range(1, n):
        #     memo[i][0] = max(memo[i - 1][0], memo[i - 1][1] + prices[i] - fee)
        #     memo[i][1] = max(memo[i - 1][0] - prices[i], memo[i - 1][1])
        # return memo[n - 1][0]
        
        #### DP with space optimization ####
        n = len(prices)
        last0, last1 = 0, -prices[0]
        for i in range(0, n):
            last0 = max(last0, last1 + prices[i] - fee)
            last1 = max(last0 - prices[i], last1)
        return last0
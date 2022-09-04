class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #### DP ####
        # n = len(prices)
        # memo = [[0,1] for i in range(n)]
        # memo[0][1] = -prices[0]
        # for i in range(1, n):
        #     memo[i][0] = max(memo[i - 1][0], memo[i - 1][1] + prices[i])
        #     memo[i][1] = max(memo[i - 1][1], memo[i - 2][0] - prices[i])
        # return memo[n - 1][0]
    
        #### DP With Space Optimization ####
        n = len(prices)
        last0, last1, last2 = 0, -prices[0], 0
        for i in range(n):
            tmp = last0
            last0 = max(last0, last1 + prices[i])
            last1 = max(last1, last2 - prices[i])
            last2 = tmp
        return last0
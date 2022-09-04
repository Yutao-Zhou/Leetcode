class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##### Brute Force #####
        # ans = 0
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         if prices[j] - prices[i] > ans:
        #             ans = prices[j] - prices[i]
        # return ans
        
        ##### one pass ######
        # minimum = 10 ** 4
        # maximum = 0
        # ans = 0
        # for i in range(0,len(prices)):
        #     if prices[i] < minimum:
        #         minimum = prices[i]
        #     if prices[i] > minimum:
        #         maximum = prices[i]
        #         if maximum - minimum > ans:
        #             ans = maximum - minimum
        # return ans
        
        #### DP ####
        # n = len(prices)
        # dp = [[0, 1] for i in range(n)]
        # for i in range(n):
        #     if i == 0:
        #         dp[i][0] = 0
        #         dp[i][1] = -prices[i]
        #     else:
        #         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #         dp[i][1] = max(-prices[i], dp[i - 1][1])
        # return dp[n - 1][0]
        
        #### DP Space Optimize ####
        n = len(prices)
        last0, last1 = 0, -prices[0]
        for i in range(n):
            last0 = max(last0, last1 + prices[i])
            last1 = max(-prices[i], last1)
        return last0
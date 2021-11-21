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
        minimum = 10 ** 4
        maximum = 0
        ans = 0
        for i in range(0,len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            if prices[i] > minimum:
                maximum = prices[i]
                if maximum - minimum > ans:
                    ans = maximum - minimum
        return ans
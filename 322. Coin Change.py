class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #### DP ####
        DP = [0] + [float('inf')] * (amount)
        for i in range(1, amount + 1):
            m = float('inf')
            for c in coins:
                if i - c >= 0:
                    m = min(DP[i - c], m)
            DP[i] = m + 1
        if DP[amount] == float('inf'):
            return -11
        return DP[amount]
class Solution:
    def numTrees(self, n: int) -> int:
        #### Recursive with memorization ####
        # def construct(n):
        #     ans = 0
        #     if n in memo:
        #         return memo[n]
        #     for l in range(n):
        #         r = n - 1 - l
        #         ans += construct(l) * construct(r)
        #     memo[n] = ans
        #     return ans
        # memo = {0: 1, 1: 1, 2: 2}
        # return construct(n)
        
        #### DP ####
        def construct(n):
            if DP[n] != 0:
                return DP[n]
            for l in range(n):
                r = n - 1 - l
                DP[n] += construct(l) * construct(r)
            return DP[n]
        DP = [1, 1, 2]
        DP.extend([0] * (n - 2))
        return construct(n)
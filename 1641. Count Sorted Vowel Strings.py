class Solution:
    def countVowelStrings(self, n: int) -> int:
        #### DP ####
        memo = [1] * 5
        for i in range(n - 1):
            cache = 0
            for i in range(4, -1, -1):
                cache += memo[i]
                memo[i] = cache
        return sum(memo)
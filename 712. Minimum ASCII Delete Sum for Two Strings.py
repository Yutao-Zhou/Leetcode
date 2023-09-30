class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        #### DP bottom up ####
        memo = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
        for i in range(1, len(memo[0])):
            memo[0][i] = memo[0][i - 1] + ord(s1[i - 1])
        for i in range(1, len(memo)):
            memo[i][0] = memo[i - 1][0] + ord(s2[i - 1])
        for y in range(1, len(memo)):
            for x in range(1, len(memo[0])):
                if s1[x - 1] == s2[y - 1]:
                    memo[y][x] = memo[y - 1][x - 1]
                else:
                    memo[y][x] = min(memo[y - 1][x] + ord(s2[y - 1]), memo[y][x - 1] + ord(s1[x - 1]))
        return memo[-1][-1]
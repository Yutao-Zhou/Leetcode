class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #### Backtrack ####
        # def backtrack(p1, p2):
        #     if p1 == len(word1):
        #         return len(word2) - p2
        #     if p2 == len(word2):
        #         return len(word1) - p1
            
        #     score = min(backtrack(p1 + 1, p2), backtrack(p1, p2 + 1), backtrack(p1 + 1, p2 + 1))
        #     if word1[p1] != word2[p2]:
        #         score += 1
        #     return score

        # return backtrack(0, 0)

        #### DP Topdown ####
        # def backtrack(p1, p2):
        #     if p1 == len(word1):
        #         return len(word2) - p2
        #     if p2 == len(word2):
        #         return len(word1) - p1
            
        #     if memo[p2][p1] == -1:
        #         if word1[p1] == word2[p2]:
        #             score = backtrack(p1 + 1, p2 + 1)
        #         else:
        #             score = min(backtrack(p1 + 1, p2), backtrack(p1, p2 + 1), backtrack(p1 + 1, p2 + 1)) + 1 
        #         memo[p2][p1] = score
        #     return memo[p2][p1]

        # memo = [[-1 for i in range(len(word1))] for j in range(len(word2))]
        # return backtrack(0, 0)

        #### DP Bottomup ####
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        memo = [[-1 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        for i in range(len(memo)):
            memo[i][0] = i
        for i in range(len(memo[0])):
            memo[0][i] = i

        for y in range(1, len(memo)):
            for x in range(1, len(memo[0])):
                if word2[y - 1] == word1[x - 1]:
                    memo[y][x] = memo[y - 1][x - 1]
                else:
                    memo[y][x] = min(memo[y - 1][x - 1], memo[y - 1][x], memo[y][x - 1]) + 1
                
        return memo[-1][-1]
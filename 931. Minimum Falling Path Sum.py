class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #### DP Bottomup ####
        memo = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        memo[0] = matrix[0]
        
        for y in range(1, len(matrix)):
            for x in range(len(matrix[0])):
                result = memo[y - 1][x] + matrix[y][x]
                if x - 1 >= 0:
                    result = min(result, memo[y - 1][x - 1] + matrix[y][x])
                if x + 1 < len(matrix[0]):
                    result = min(result, memo[y - 1][x + 1] + matrix[y][x])
                memo[y][x] = result
        
        return min(memo[-1])
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        j = 0
        ans = 0
        
        for i in range(len(mat)):
                ans += mat[i][j]
                ans += mat[i][-j - 1]
                j += 1
        if len(mat) % 2 != 0:
            ans -= mat[len(mat) // 2][-len(mat) // 2]
        return ans
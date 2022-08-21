class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        #### Brute Force ####
        # ans, lx, ly = [], len(mat[0]), len(mat)
        # row = []
        # for r in range(lx):
        #     row.append(0)
        # for r in range(ly):
        #     ans.append(row.copy())
        # for y in range(ly):
        #     for x in range(lx):
        #         s = 0
        #         for j in range(y - k, y + k + 1):
        #             for i in range(x - k, x + k + 1):
        #                 if 0 <= i <= lx - 1 and 0 <= j <= ly - 1:
        #                     s += mat[j][i]
        #         ans[y][x] = s
        # return ans
        
        #### Prefix Sum ####
        n, m = len(mat[0]), len(mat)
        prefMat= [[0] * n for _ in range(m)]
        for j in range(m):
            preX = 0
            for i in range(n):
                preX += mat[j][i]
                prefMat[j][i] = preX
        for i in range(n):
            preX = 0
            for j in range(m):
                preX += prefMat[j][i]
                prefMat[j][i] = preX
        for i in range(m):
            ru = max(i - k, 0)
            rd = min(i + k, m - 1)
            for j in range(n):
                cl = max(0, j - k)
                cr = min(n - 1, j + k)
                value = prefMat[rd][cr]
                if ru - 1 >= 0:
                    value -= prefMat[ru - 1][cr]
                if cl - 1 >= 0:
                    value -= prefMat[rd][cl - 1]
                if ru - 1 >= 0 and cl - 1 >= 0:
                    value += prefMat[ru - 1][cl - 1]
                mat[i][j] = value
        return mat
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        #### simulation ####
        ans = []
        odd = 0
        for i in range(m):
            ans += [[0] * n]
        for cordinate in indices:
            for j in range(len(ans[cordinate[0]])):
                ans[cordinate[0]][j] += 1
            for k in ans:
                k[cordinate[1]] += 1
        for i in ans:
            for j in i:
                if j % 2 == 1:
                    odd += 1
        return odd
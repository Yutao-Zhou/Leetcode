class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        #### Backtrack ####
        def backtrack(x, y):
            if x < 0 or y < 0 or x == n or y == m:
                return 0
            if grid[y][x] == 0:
                return 0
            ans = 0
            gold = grid[y][x]
            grid[y][x] = 0
            ans = max(ans, backtrack(x - 1, y), backtrack(x + 1, y), backtrack(x, y - 1), backtrack(x, y + 1)) + gold
            grid[y][x] = gold
            return ans
        ans = 0
        n, m = len(grid[0]), len(grid)
        for i in range(n):
            for j in range(m):
                ans = max(ans, backtrack(i, j))
        return ans
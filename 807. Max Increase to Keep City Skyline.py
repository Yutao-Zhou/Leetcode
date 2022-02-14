class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        i = 0
        ans = 0
        maxV = []
        maxH = []
        cache = 0
        for k in grid:
            maxH.append(max(k))
        while i < len(grid):
            for j in grid:
                if j[i] > cache:
                    cache = j[i]
            maxV.append(cache)
            cache = 0
            i += 1
        for a in range(len(grid)):
            for b in range(len(grid[a])):
                ans += min(maxV[a],maxH[b]) - grid[a][b]
        return ans
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        l = [0]*len(grid[0])
        grid.insert(0,l)
        grid.append(l)
        for i in grid:
            i.insert(0,0)
            i.append(0)
        for i in range(0,len(grid)-1,1):
            for j in range(0,len(grid[i]),1):
                k = grid[i]
                a = grid[i-1]
                b = grid[i+1]
                if k[j] == 1:
                    if k[j-1] == 0 or j == 0:
                           ans += 1
                    if k[j+1] == 0:
                           ans += 1
                    if a[j] == 0 or i == 0:
                           ans += 1
                    if b[j] == 0:
                           ans += 1
        return ans
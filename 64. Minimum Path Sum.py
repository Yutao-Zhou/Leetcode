class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #### DFS Brute Force ####
        # ans, stack = float('inf'), [(0, 0, grid[0][0])]
        # ly, lx = len(grid) - 1, len(grid[0]) - 1
        # while stack:
        #     node = stack.pop()
        #     if node[0] == ly and node[1] == lx:
        #         ans = min(ans, node[2])
        #         continue
        #     if node[0] + 1 <= ly:
        #         stack.append((node[0] + 1, node[1], node[2] + grid[node[0] + 1][node[1]]))
        #     if node[1] + 1 <= lx:
        #         stack.append((node[0], node[1] + 1, node[2] + grid[node[0]][node[1] + 1]))
        # return ans
        
        #### DP ####
        ly, lx = len(grid), len(grid[0])
        for i in range(ly):
            for j in range(lx):
                if i == 0 and j == 0:
                    continue
                cur = float('inf')
                if j - 1 >= 0:
                    cur = min(cur, grid[i][j - 1])
                if i - 1 >= 0:
                    cur = min(cur, grid[i - 1][j])
                grid[i][j] += cur
        return grid[-1][-1]
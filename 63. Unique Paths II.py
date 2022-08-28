class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #### DFS Brute forece ####
        # target = (len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)
        # if obstacleGrid[target[0]][target[1]] or obstacleGrid[0][0]:
        #     return 0
        # ans, stack = 0, [(0, 0)]
        # while stack:
        #     node = stack.pop()
        #     if node == target:
        #         ans += 1
        #     if 0 <= node[0] + 1 <= target[0] and obstacleGrid [node[0] + 1][node[1]] != 1:
        #         stack.append((node[0] + 1, node[1]))
        #     if 0 <= node[1] + 1 <= target[1] and obstacleGrid [node[0]][node[1] + 1] != 1:
        #         stack.append((node[0], node[1] + 1))
        # return ans
        
        #### DP ####
        ly, lx = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(ly):
            for j in range(lx):
                if i == 0 and j == 0:
                    obstacleGrid[0][0] = 1
                    continue
                cur = 0
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                if 0 < i:
                    cur += obstacleGrid[i - 1][j]
                if 0 < j:
                    cur += obstacleGrid[i][j - 1]
                obstacleGrid[i][j] = cur
        return obstacleGrid[-1][-1]
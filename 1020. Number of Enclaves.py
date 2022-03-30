class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #### BFS ####
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    que = deque()
                    que.append((i,j))
                    touch = False
                    area = 0
                    while que:
                        p = que.popleft()
                        if 0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0]):
                            if grid[p[0]][p[1]] == 1:
                                area += 1
                                grid[p[0]][p[1]] = 0
                                if p[0] == 0 or p[0] == len(grid) - 1 or p[1] == 0 or p[1] == len(grid[0]) - 1:
                                    touch = True
                                que.append((p[0] - 1, p[1]))
                                que.append((p[0], p[1] + 1))
                                que.append((p[0] + 1, p[1]))
                                que.append((p[0], p[1] - 1))
                    if not touch:
                        ans += area
        return ans
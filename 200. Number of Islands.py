class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #### BFS ####
        # from collections import deque
        # ans = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         que = deque()
        #         if grid[i][j] == "1":
        #             que.append((i,j))
        #             while que:
        #                 node = que.popleft()
        #                 if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[i]) and grid[node[0]][node[1]] == "1":
        #                     grid[node[0]][node[1]] = "-1"
        #                     que.append((node[0] - 1, node[1]))
        #                     que.append((node[0], node[1] + 1))
        #                     que.append((node[0] + 1, node[1]))
        #                     que.append((node[0], node[1] - 1))
        #             ans += 1
        # return ans
        
        #### DFS ####
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                stack = []
                if grid[i][j] == "1":
                    stack.append((i,j))
                    while stack:
                        node = stack.pop()
                        if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[i]) and grid[node[0]][node[1]] == "1":
                            grid[node[0]][node[1]] = "-1"
                            stack.append((node[0] - 1, node[1]))
                            stack.append((node[0], node[1] + 1))
                            stack.append((node[0] + 1, node[1]))
                            stack.append((node[0], node[1] - 1))
                    ans += 1
        return ans
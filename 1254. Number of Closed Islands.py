class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        #### BFS ####
        ans = 0
        que = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    que.append((i,j))
                    count = True
                    while que:
                        node = que.popleft()
                        if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0]):
                            if grid[node[0]][node[1]] == 0:
                                grid[node[0]][node[1]] = -1
                                que.append((node[0] - 1, node[1]))
                                que.append((node[0], node[1] + 1))
                                que.append((node[0] + 1, node[1]))
                                que.append((node[0], node[1] - 1))
                                if node[0] == 0 or node[0] == len(grid) - 1 or node[1] == 0 or node[1] == len(grid[0]) - 1:
                                    count = False
                    if count == True:
                        ans += 1
        return ans
    
        #### DFS ####
        # ans = 0
        # stack = []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 0:
        #             stack.append((i,j))
        #             count = True
        #             while stack:
        #                 node = stack.pop()
        #                 if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0]):
        #                     if grid[node[0]][node[1]] == 0:
        #                         grid[node[0]][node[1]] = -1
        #                         stack.append((node[0] - 1, node[1]))
        #                         stack.append((node[0], node[1] + 1))
        #                         stack.append((node[0] + 1, node[1]))
        #                         stack.append((node[0], node[1] - 1))
        #                         if node[0] == 0 or node[0] == len(grid) - 1 or node[1] == 0 or node[1] == len(grid[0]) - 1:
        #                             count = False
        #             if count == True:
        #                 ans += 1
        # return ans
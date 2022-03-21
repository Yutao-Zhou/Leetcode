class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        #### BFS ####
        # seen = set()
        # que = deque()
        # que.append((row,col))
        # start = grid[row][col]
        # if start == color:
        #     return grid
        # while que:
        #     node = que.popleft()
        #     if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0]):
        #         if grid[node[0]][node[1]] == start and node not in seen:
        #             seen.add(node)
        #             que.append((node[0] - 1,node[1]))
        #             que.append((node[0],node[1] + 1))
        #             que.append((node[0] + 1,node[1]))
        #             que.append((node[0],node[1] - 1))
        #             if (node[0] == 0 or node[0] == len(grid) - 1) or (node[1] == 0 or node[1] == len(grid[0]) - 1):
        #                 grid[node[0]][node[1]] = color
        #             else:
        #                 if grid[node[0] - 1][node[1]] != start and (node[0] - 1,node[1]) not in seen:
        #                     grid[node[0]][node[1]] = color
        #                 if grid[node[0]][node[1] + 1] != start and (node[0],node[1] + 1) not in seen:
        #                     grid[node[0]][node[1]] = color
        #                 if grid[node[0] + 1][node[1]] != start and (node[0] + 1,node[1]) not in seen:
        #                     grid[node[0]][node[1]] = color
        #                 if grid[node[0]][node[1] - 1] != start and (node[0],node[1] - 1) not in seen:
        #                     grid[node[0]][node[1]] = color
        # return grid
    
        #### DFS ####
        seen = set()
        stack = []
        stack.append((row,col))
        start = grid[row][col]
        if start == color:
            return grid
        while stack:
            node = stack.pop()
            if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0]):
                if grid[node[0]][node[1]] == start and node not in seen:
                    seen.add(node)
                    stack.append((node[0] - 1,node[1]))
                    stack.append((node[0],node[1] + 1))
                    stack.append((node[0] + 1,node[1]))
                    stack.append((node[0],node[1] - 1))
                    if (node[0] == 0 or node[0] == len(grid) - 1) or (node[1] == 0 or node[1] == len(grid[0]) - 1):
                        grid[node[0]][node[1]] = color
                    else:
                        if grid[node[0] - 1][node[1]] != start and (node[0] - 1,node[1]) not in seen:
                            grid[node[0]][node[1]] = color
                        if grid[node[0]][node[1] + 1] != start and (node[0],node[1] + 1) not in seen:
                            grid[node[0]][node[1]] = color
                        if grid[node[0] + 1][node[1]] != start and (node[0] + 1,node[1]) not in seen:
                            grid[node[0]][node[1]] = color
                        if grid[node[0]][node[1] - 1] != start and (node[0],node[1] - 1) not in seen:
                            grid[node[0]][node[1]] = color
        return grid
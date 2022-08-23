class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #### Iteritive BFS ####
        def rotting():
            time, visited = 0, set()
            while queue:
                node = queue.popleft()
                if grid[node[0]][node[1]] == 2:
                    if (node[0], node[1]) not in visited:
                        visited.add((node[0], node[1]))
                        time = max(time, node[2])
                        if 0 <= node[0] - 1:
                            if grid[node[0] - 1][node[1]] == 1:
                                grid[node[0] - 1][node[1]] = 2
                                queue.append((node[0] - 1, node[1], node[2] + 1))
                        if node[0] + 1 < len(grid):
                            if grid[node[0] + 1][node[1]] == 1:
                                grid[node[0] + 1][node[1]] = 2
                                queue.append((node[0] + 1, node[1], node[2] + 1))
                        if 0 <= node[1] - 1:
                            if grid[node[0]][node[1] - 1] == 1:
                                grid[node[0]][node[1] - 1] = 2
                                queue.append((node[0], node[1] - 1, node[2] + 1))
                        if node[1] + 1 < len(grid[0]):
                            if grid[node[0]][node[1] + 1] == 1:
                                grid[node[0]][node[1] + 1] = 2
                                queue.append((node[0], node[1] + 1, node[2] + 1))
            for l in grid:
                if 1 in l:
                    return -1
            return time
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        return rotting()
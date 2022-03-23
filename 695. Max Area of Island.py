class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #### BFS ####
        # ans = 0
        # que = deque()
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             que.append((i,j))
        #             area = 0
        #             while que:
        #                 node = que.popleft()
        #                 if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0]):
        #                     if grid[node[0]][node[1]] == 1:
        #                         grid[node[0]][node[1]] = 0
        #                         area += 1
        #                         que.append((node[0] - 1, node[1]))
        #                         que.append((node[0], node[1] + 1))
        #                         que.append((node[0] + 1, node[1]))
        #                         que.append((node[0], node[1] - 1))
        #             if area > ans:
        #                 ans = area
        # return ans
        
        #### recursive BFS ####
        s = []
        seen = set()
        def area(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i,j) not in seen:
                if grid[i][j] == 1:
                    seen.add((i,j))
                    return (1 + area(i - 1, j) + area(i, j + 1) + area(i + 1, j) + area(i, j - 1))
                else:
                    return 0
            else:
                return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                s.append(area(i,j))
        return max(s)
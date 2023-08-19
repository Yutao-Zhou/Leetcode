class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        #### BFS from every water ####
        # ans = -1
        # n = len(grid)
        # dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # no_land = True
        # for y in range(n):
        #     for x in range(n):
        #         if grid[y][x] == 1:
        #             no_land = False
        #             break
        #     if not no_land:
        #         break
        # if no_land:
        #     return ans
        # for y in range(n):
        #     for x in range(n):
        #         if grid[y][x] == 0:
        #             seen = set()
        #             queue = deque()
        #             queue.append((y, x, 0))
        #             while queue:
        #                 current = queue.popleft()
        #                 if (current[0], current[1]) not in seen:
        #                     for direction in dydx:
        #                         if 0 <= current[0] + direction[0] < n and 0 <= current[1] + direction[1] < n:
        #                             if grid[current[0] + direction[0]][current[1] + direction[1]] == 1:
        #                                 ans = max(ans, current[2] + 1)
        #                                 queue = deque()
        #                                 break
        #                             else:
        #                                 queue.append((current[0] + direction[0], current[1] + direction[1], current[2] + 1))
        #                 seen.add((current[0], current[1]))
        # return ans

        #### BFS from every land ####
        seen = set()
        queue = deque()
        ans = -1
        n = len(grid)
        dydx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for y in range(n):
            for x in range(n):
                if grid[y][x] == 1:
                    queue.append((y, x, 0))
        while queue:
            current = queue.popleft()
            if (current[0], current[1]) not in seen:
                if grid[current[0]][current[1]] == 0:
                    ans = current[2]
                for direction in dydx:
                    if 0 <= current[0] + direction[0] < n and 0 <= current[1] + direction[1] < n and grid[current[0] + direction[0]][current[1] + direction[1]] == 0:
                        queue.append((current[0] + direction[0], current[1] + direction[1], current[2] + 1))
            seen.add((current[0], current[1]))
        return ans
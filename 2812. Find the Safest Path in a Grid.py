class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        #### BFS + Binary Search ####
        # queue = deque()
        # n = len(grid)
        # seen = set()
        # for y in range(n):
        #     for x in range(n):
        #         if grid[y][x] == 1:
        #             queue.append((y, x, 0))
        # while queue:
        #     y, x, distance = queue.popleft()
        #     if (y, x) not in seen:
        #         seen.add((y, x))
        #         grid[y][x] = distance
        #         if 0 <= y - 1 < n:
        #             queue.append((y - 1, x, distance + 1))
        #         if 0 <= x + 1 < n:
        #             queue.append((y, x + 1, distance + 1))
        #         if 0 <= y + 1 < n:
        #             queue.append((y + 1, x, distance + 1))
        #         if 0 <= x - 1 < n:
        #             queue.append((y, x - 1, distance + 1))
        # l, h = 0, n - 1
        # while l < h:
        #     mid = (h + l + 1) // 2
        #     queue = [(0, 0)]
        #     seen = set()
        #     success = False
        #     while queue:
        #         y, x = queue.pop()
        #         if (y, x) not in seen:
        #             seen.add((y, x))
        #             if grid[y][x] >= mid:
        #                 if (y, x) == (n - 1, n - 1):
        #                     success = True
        #                 if 0 <= y - 1 < n:
        #                     queue.append((y - 1, x))
        #                 if 0 <= x + 1 < n:
        #                     queue.append((y, x + 1))
        #                 if 0 <= y + 1 < n:
        #                     queue.append((y + 1, x))
        #                 if 0 <= x - 1 < n:
        #                     queue.append((y, x - 1))
        #     if success:
        #         l = mid
        #     else:
        #         h = mid - 1
        # return l

        #### BFS + BFS ####
        ans = 0
        queue = deque()
        n = len(grid)
        seen = set()
        for y in range(n):
            for x in range(n):
                if grid[y][x] == 1:
                    queue.append((y, x, 0))
        while queue:
            y, x, distance = queue.popleft()
            if (y, x) not in seen:
                seen.add((y, x))
                grid[y][x] = distance
                if 0 <= y - 1 < n:
                    queue.append((y - 1, x, distance + 1))
                if 0 <= x + 1 < n:
                    queue.append((y, x + 1, distance + 1))
                if 0 <= y + 1 < n:
                    queue.append((y + 1, x, distance + 1))
                if 0 <= x - 1 < n:
                    queue.append((y, x - 1, distance + 1))

        queue = deque([(0, 0, grid[0][0])])
        seen = set()
        while queue:
            y, x, score = queue.popleft()
            if (y, x, score) not in seen:
                seen.add((y, x, score))
                score = min(score, grid[y][x])
                if (y, x) == (n - 1, n - 1):
                    ans = max(ans, score)
                if 0 <= y - 1 < n:
                    queue.append((y - 1, x, score))
                if 0 <= x + 1 < n:
                    queue.append((y, x + 1, score))
                if 0 <= y + 1 < n:
                    queue.append((y + 1, x, score))
                if 0 <= x - 1 < n:
                    queue.append((y, x - 1, score))
        return ans
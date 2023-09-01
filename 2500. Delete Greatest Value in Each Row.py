class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        #### sort ####
        # ans = 0
        # for i in range(len(grid)):
        #     grid[i].sort()
        # for x in range(len(grid[0])):
        #     max_n = 0
        #     for row in grid:
        #         max_n = max(max_n, row[x])
        #     ans += max_n
        # return ans

        #### heap simulation ####
        import heapq
        ans = 0
        for i in range(len(grid)):
            heap_row = []
            for j in range(len(grid[i])):
                heapq.heappush(heap_row, -grid[i][j])
            grid[i] = heap_row
        while grid[0]:
            max_n = 0
            for row in grid:
                max_n = min(max_n, heapq.heappop(row))
            ans += -max_n
        return ans
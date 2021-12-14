class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ##### really doing it #####
        # numbers = []
        # ans = []
        # c = 0
        # mc = 1
        # m = len(grid)
        # n = len(grid[0])
        # for i in grid:
        #     for j in i:
        #         numbers.append(j)
        # while c < k:
        #     numbers.insert(0,numbers[-1])
        #     numbers.pop()
        #     c += 1
        # while mc <= m:
        #     ans.append(numbers[(mc - 1) * n: mc * n])
        #     mc += 1
        # return ans
    
        ##### read and write #####
        ans = []
        cach = []
        counter = 0
        m = len(grid)
        n = len(grid[0])
        mi = (m - 1 - (k - 1) // n) % m
        ni = (n - k) % n
        while 1:
            if counter > m * n:
                return ans
            if len(cach) == n:
                ans.append(cach)
                cach = []
            cach.append(grid[mi][ni])
            counter += 1
            ni += 1
            if ni == n:
                ni = 0
                mi += 1
            if mi == m :
                mi = 0
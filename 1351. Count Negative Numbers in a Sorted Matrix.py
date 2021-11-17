class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # ans = 0
        # for i in grid:
        #     for j in range(-1,-len(i) - 1,-1):
        #         if i[j] < 0:
        #             ans += 1
        #         else:
        #             break
        # return ans
        k = -1
        ans = 0
        for i in range(len(grid)):
            for j in range(k,-len(grid[i]) - 1,-1):
                if grid[i][j] < 0:
                    k -= 1
                    ans += len(grid) - i
                else:
                    break
        return ans
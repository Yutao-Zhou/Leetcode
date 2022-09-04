class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #### Backtrack ####
        # ans = []
        # path = []
        # def backtrack(start = 9):
        #     if len(path) == k:
        #         if sum(path) == n:
        #             ans.append(path[:])
        #         return
        #     for i in range(start, 0, -1):
        #         path.append(i)
        #         backtrack(i - 1)
        #         path.pop()
        # backtrack()
        # return ans
        
        #### Backtrack with earlier stop ####
        ans = []
        path = []
        def backtrack(start = 1):
            if len(path) == k or sum(path) > n:
                if sum(path) == n:
                    ans.append(path[:])
                return
            for i in range(start, min(10, n + 1)):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        backtrack()
        return ans
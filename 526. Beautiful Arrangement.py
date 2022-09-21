class Solution:
    def countArrangement(self, n: int) -> int:
        #### Backtrack Generate and Check ####
        # def backtrack(path, remain):
        #     if not remain:
        #         beautiful = True
        #         for idx, num in enumerate(path):
        #             if num % (idx + 1) and (idx + 1) % num:
        #                 beautiful = False
        #                 break
        #         if beautiful:
        #             self.ans += 1
        #         return
        #     for i in range(len(remain)):
        #         backtrack(path + [remain[i]], remain[:i] + remain[i + 1:])
        # self.ans = 0
        # backtrack([], list(range(1,n + 1)))
        # return self.ans
        
        #### Backtrack With Early Stop ####
        #### Backtrack Generate and Check ####
        def backtrack(path, remain):
            if not remain:
                self.ans += 1
                return
            lenPath = len(path)
            for i in range(n - lenPath):
                if not remain[i] % (lenPath + 1) or not (lenPath + 1) % remain[i]:
                    backtrack(path + [remain[i]], remain[:i] + remain[i + 1:])
        self.ans = 0
        backtrack([], list(range(1,n + 1)))
        return self.ans
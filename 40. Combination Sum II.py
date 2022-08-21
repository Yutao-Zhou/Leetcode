class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #### Clasic Backtrack ####
        # ans, l = [], len(candidates)
        # candidates = sorted(candidates)
        # def backtrack(start, target, current):
        #     if target < 0:
        #         return
        #     if target == 0:
        #         ans.append(current.copy())
        #         return
        #     for i in range(start, l):
        #         if i != start and candidates[i] == candidates[i - 1]:
        #             continue
        #         backtrack(i + 1, target - candidates[i], current + [candidates[i]])
        # backtrack(0, target, [])
        # return ans
        
        #### little improved Backtrack ####
        ans, stop = [], len(candidates)
        candidates = sorted(candidates)
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] > target:
                stop = i
        def backtrack(start, target, current):
            if target < 0:
                return
            if target == 0:
                ans.append(current.copy())
                return
            for i in range(start, stop):
                if i != start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, target - candidates[i], current + [candidates[i]])
        backtrack(0, target, [])
        return ans
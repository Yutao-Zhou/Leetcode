class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #### standard backtrack ####
        def backtrack(i, target, current):
            if target == 0:
                ans.append(current.copy())
            if target < 0:
                return
            for i in range(i, len(candidates)):
                current.append(candidates[i])
                backtrack(i, target - candidates[i], current)
                current.pop()
        ans = []
        backtrack(0, target, [])
        return ans
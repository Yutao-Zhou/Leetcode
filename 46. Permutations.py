class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #### Backtrack ####
        ans, l = [], len(nums)
        def backtrack(current, cl, remain):
            if cl == l:
                ans.append(current)
                return
            else:
                for i in range(len(remain)):
                    backtrack(current + [remain[i]], cl + 1, remain[:i] + remain[i + 1:])
        backtrack([], 0, nums)
        return ans
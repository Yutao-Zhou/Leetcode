class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #### Backtrack brute force check repeat ####
        # ans, l = [], len(nums)
        # def backtrack(current, cl, remain):
        #     if cl == l:
        #         if current not in ans:
        #             ans.append(current)
        #         return
        #     else:
        #         for i in range(len(remain)):
        #             backtrack(current + [remain[i]], cl + 1, remain[:i] + remain[i + 1:])
        # backtrack([], 0, nums)
        # return ans
        
        #### Backtrack Skip Duplicate Starts ####
        ans, l = [], len(nums)
        nums.sort()
        def backtrack(current, cl, remain):
            if not remain:
                ans.append(current)
                return
            else:
                for i in range(len(remain)):
                    if i > 0 and remain[i] == remain[i - 1]:
                        continue
                    backtrack(current + [remain[i]], cl + 1, remain[:i] + remain[i + 1:])
        backtrack([], 0, nums)
        return ans
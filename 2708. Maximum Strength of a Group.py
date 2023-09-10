class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        #### Greedy ####
        # nums.sort()
        # if len(nums) == 1:
        #     return nums[0]
        # non_zero = False
        # ans = 1
        # j = len(nums) - 1
        
        # while j >= 0 and nums[j] > 0:
        #     non_zero = True
        #     ans *= nums[j]
        #     j -= 1
        # while j >= 0 and nums[j] >= 0:
        #     j -= 1
        # if j % 2 == 0:
        #     j -= 1
        # for i in range(j + 1):
        #     non_zero = True
        #     ans *= nums[i]
        # if not non_zero:
        #     return 0
        # return ans

        #### Backtrack ####
        def checkResult(i, score=None):
            if i == len(nums) and score != None:
                nonlocal ans
                ans = max(score, ans)
                return
            if i < len(nums):
                if score:
                    checkResult(i + 1, score)
                    checkResult(i + 1, score * nums[i])
                else:
                    checkResult(i + 1, None)
                    checkResult(i + 1, nums[i])
        
        ans = nums[0]
        checkResult(0)
        return ans
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        #### Monotonic Stack ####
        stack = []
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            score = 0
            while stack and nums[i] > stack[-1][0]:
                n, s = stack.pop()
                if s > score:
                    score = s
                else:
                    score += 1
            stack.append((nums[i], score))
            ans = max(ans, score)
        return ans
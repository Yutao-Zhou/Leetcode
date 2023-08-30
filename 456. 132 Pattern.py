class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #### Brute Force ####
        # lenNums = len(nums)
        # for i in range(lenNums - 2):
        #     for j in range(i + 1, lenNums - 1):
        #         for k in range(j + 1, lenNums):
        #             if nums[i] < nums[k] < nums[j]:
        #                 return True
        # return False

        # Monotonic Stack
        stack = []
        min_seen = [-1] * len(nums)
        min_seen[0] = nums[0]
        for i in range(1, len(nums)):
            min_seen[i] = min(min_seen[i - 1], nums[i])

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= min_seen[i]:
                continue
            while stack and min_seen[i] >= stack[-1]:
                stack.pop()
            if stack and stack[-1] < nums[i]:
                return True
            stack.append(nums[i])
        return False
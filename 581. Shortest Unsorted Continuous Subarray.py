class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #### Monotonic Stack ####
        unsort_min_index = len(nums) - 1
        if unsort_min_index == 0:
            return 0
        unsort_max_index = 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                unsort_min_index = min(unsort_min_index, stack.pop())
            stack.append(i)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                unsort_max_index = max(unsort_max_index, stack.pop())
            stack.append(i)
        return max(0, unsort_max_index - unsort_min_index + 1)
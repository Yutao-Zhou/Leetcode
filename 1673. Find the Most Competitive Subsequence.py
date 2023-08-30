class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        #### Monotonic Stack ####
        stack = []
        nums.append(-1)
        len_nums = len(nums)
        for i in range(len_nums):
            while stack and nums[i] < stack[-1] and len_nums - i + len(stack) - 1 > k:
                stack.pop()
            stack.append(nums[i])
        return stack[:-1]
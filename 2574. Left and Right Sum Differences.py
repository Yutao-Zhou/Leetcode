class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        ans = [0] * len_nums
        left_sum = [0]
        right_sum = 0
        for n in nums:
            left_sum.append(left_sum[-1] + n)
        for i in range(len_nums - 1, -1, -1):
            ans[i] = abs(left_sum[i] - right_sum)
            right_sum += nums[i]
        return ans
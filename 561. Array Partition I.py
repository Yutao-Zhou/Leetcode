class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = -2
        ans = 0
        while 1:
            if i == -len(nums) - 2:
                return ans
            ans += nums[i]
            i -= 2
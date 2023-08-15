class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        l, r = 0, 0
        n = len(nums)
        zero = 0
        while l < n and r < n:
            if nums[r] == 0:
                zero += 1
                if zero > k:
                    ans = max(ans, r - l)
                while zero > k:
                    if nums[l] == 0:
                        zero -= 1
                    l += 1
            r += 1
        return max(ans, r - l)
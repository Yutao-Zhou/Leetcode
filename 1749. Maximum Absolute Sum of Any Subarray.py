class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0
        pos = 0
        neg = 0
        for n in nums:
            pos = max(pos + n, 0)
            neg = min(neg + n, 0)
            ans = max(ans, abs(pos + neg))
        return ans
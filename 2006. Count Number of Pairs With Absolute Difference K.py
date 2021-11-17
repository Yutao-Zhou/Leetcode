class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        for j in range(1,len(nums)):
            for i in range(0,j):
                if abs(nums[i]-nums[j]) == k:
                    ans += 1
        return ans
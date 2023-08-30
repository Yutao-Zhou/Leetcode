class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_nums = 0
        ans = 0
        for i in range(len(arr)):
            max_nums = max(max_nums, arr[i])
            if i == max_nums:
                ans += 1
        return ans
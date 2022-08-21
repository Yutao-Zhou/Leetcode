class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #### Sliding windows ####
        l, windowSize, lnums, minSwap = 0, sum(nums), len(nums), float('inf')
        if l == (l + windowSize) % lnums:
            return 0
        curSwap = windowSize - sum(nums[l: l + (l + windowSize) % lnums])
        for l in range(lnums):
            if nums[l] == 0 and nums[(l + windowSize) % lnums] == 1:
                curSwap -= 1
            if nums[l] == 1 and nums[(l + windowSize) % lnums] == 0:
                curSwap += 1
            minSwap = min(minSwap, curSwap)
        return minSwap
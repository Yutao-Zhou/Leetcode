class Solution:
    def findMin(self, nums: List[int]) -> int:
        #### binary search ####
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[l] < nums[mid]:
                l = mid
            if nums[l] > nums[mid]:
                r = mid
        return nums[r]
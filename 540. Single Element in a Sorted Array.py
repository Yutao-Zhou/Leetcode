class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #### Two Pointers Bunary Search ####
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l]
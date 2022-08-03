class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #### prefix or suffix ####
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            if nums[i - 1]:
                nums[i] *= nums[i - 1]
            if reverse[i - 1]:
                reverse[i] *= reverse[i - 1]
        return max(nums + reverse)
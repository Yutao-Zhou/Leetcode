class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #### check one by one ####
        if max(nums) - min(nums) == 0:
            return True
        increase = False
        if max(nums) - min(nums) > 0 and nums[0] != max(nums):
            increase = True
        for i in range(1,len(nums)):
            if nums[i] - nums[i - 1] < 0 and increase == True:
                return False
            if nums[i] - nums[i - 1] > 0 and increase == False:
                return False
        return True
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        #### check to pop this one or previous one ####
        faile = 0
        if nums[1] <= nums[0]:
            faile += 1
        nums.append(1001)
        for i in range(2,len(nums) - 1):
            if nums[i] <= nums[i - 1]:
                faile += 1
                if nums[i] > nums[i - 2] or nums[i + 1] > nums[i - 1]:
                    continue
                else:
                    faile += 1
        if faile > 1:
            return False
        return True
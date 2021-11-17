class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        cach = 0
        if len(nums) != 1:
            while 1:
                print(nums,i,j)
                if i == len(nums) - 1 and j == len(nums):
                    break
                if j != len(nums):
                    if nums[i] > nums[j]:
                        cach = nums[i]
                        nums[i] = nums[j]
                        nums[j] = cach
                    if nums[i] <= nums[j]:
                        j += 1
                else:
                    i += 1
                    j = i + 1
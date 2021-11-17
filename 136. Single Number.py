class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.insert(0,"")
        nums.insert(0,"")
        nums.append("")
        nums.append("")
        print(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i+1] or nums[i] == nums[i-1]:
                pass 
            else:
                return nums[i]
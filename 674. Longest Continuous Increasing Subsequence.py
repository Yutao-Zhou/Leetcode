class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        counter = 1
        ans = []
        nums.append(0)
        for i in range(1,len(nums)):
            print(nums[i],counter)
            if nums[i] > nums[i-1]:
                counter += 1
            else:
                ans.append(counter)
                counter = 1
        return max(ans)
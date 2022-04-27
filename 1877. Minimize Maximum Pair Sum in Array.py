class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        #### sort and pair ####
        ans = 0
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > ans:
                ans = nums[i] + nums[j]
            i += 1
            j -= 1
        return ans
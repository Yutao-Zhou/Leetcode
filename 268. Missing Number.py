class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #### sort and count ####
        # nums = sorted(nums)
        # if nums[0] != 0:
        #     return 0
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i - 1] + 1:
        #         return nums[i - 1] + 1
        # return nums[-1] + 1
        
        #### find right sum and subtraction ####
        # return int(len(nums) * (len(nums) + 1) / 2 - sum(nums))
    
        #### set difference ####
        check = set(list(range(max(nums) + 1)))
        nums = set(nums)
        ans = list(check.difference(nums))
        if len(ans) != 0:
            return ans[0]
        else:
            nums = sorted(list(nums))
            if nums[0] != 0:
                return 0
            else:
                return nums[-1] + 1
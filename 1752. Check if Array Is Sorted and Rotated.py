class Solution:
    def check(self, nums: List[int]) -> bool:
        #### rotate and check ####
        # for i in range(len(nums)):
        #     if nums[i:] + nums[:i] == sorted(nums):
        #         return True
        # return False
        
        #### check difference ####
        hit = 0
        if len(nums) < 3:
            return True
        for i in range(1,len(nums)):
            if nums[i] < nums[i - 1]:
                hit += 1
                if nums[-1] > nums[0]:
                    hit += 1
        if hit > 1:
            return False
        return True
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #### set ####
        # appeared = set()
        # for n in nums:
        #     if n in appeared:
        #         return True
        #     else:
        #         appeared.add(n)
        # return False
        
        #### sort ####
        # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False
        
        #### set len ####
        return len(set(nums)) != len(nums)
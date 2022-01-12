class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        #### two pointer ####
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] == 1 and nums[i] != 1:
                i = j
                j += 1
            if nums[i] == nums[j] == 1:
                if j - i - 1 < k:
                    return False
                else:
                    i = j
                    j += 1
            j += 1
        return True
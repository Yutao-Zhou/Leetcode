class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        #### save two ####
        now = (float("-inf"), 0)
        last = float("-inf")
        for i in range(len(nums)):
            if nums[i] > now[0]:
                last = now[0]
                now = (nums[i], i)
            if now[0] > nums[i] > last:
                last = nums[i]
        if now[0] >= last * 2:
            return now[1]
        return -1
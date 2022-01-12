class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        #### start from left save shortest distance ####
        # ans = 1000
        # for i in range(len(nums)):
        #     if nums[i] == target and abs(i - start) < ans:
        #         ans = abs(i - start)
        # return ans
        
        #### start from "start" and move both direction ####
        i = start
        j = start
        while 1:
            if nums[i] == target:
                return start - i
            if nums[j] == target:
                return j - start
            if i > 0:
                i -= 1
            if j < len(nums) - 1:
                j += 1
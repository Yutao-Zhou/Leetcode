class Solution:
    def findGCD(self, nums: List[int]) -> int:
        #### check ####
        ans = min(nums)
        while ans > 0 :
            if max(nums) % ans != 0 or min(nums) % ans != 0:
                    ans -= 1
            if max(nums) % ans == 0 and min(nums) % ans == 0:
                    return ans
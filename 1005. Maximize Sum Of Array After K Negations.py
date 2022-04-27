class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        #### greedy iteritive ####
        nums = sorted(nums)
        i = 0
        while k:
            if nums[i] >= 0 or i == len(nums) - 1:
                if k % 2 == 0:
                    k = 0
                else:
                    if abs(nums[i - 1]) < nums[i]:
                        nums[i - 1] = -nums[i - 1]
                        k = 0
                    else:
                        nums[i] = -nums[i]
                        k = 0
            elif nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
                i += 1 
        return sum(nums)
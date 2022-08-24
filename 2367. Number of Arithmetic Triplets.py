class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        #### Brute Force n * 3 ####
        # ans, l = 0, len(nums)
        # for i in range(l):
        #     for j in range(i + 1, l):
        #         for k in range(j + 1, l):
        #             if nums[k] - nums[j] == nums[j] - nums[i] and nums[j] - nums[i] == diff:
        #                 ans += 1
        # return ans
    
        #### Three Pointer ####
        # ans, i, j, k = 0, 0, 1, 2
        # while k < len(nums):
        #     if nums[j] - nums[i] < diff:
        #         j += 1
        #         while j >= k:
        #             k += 1
        #         pass
        #     elif nums[j] - nums[i] > diff:
        #         i += 1
        #         pass
        #     else:
        #         if nums[k] - nums[j] < diff:
        #             k += 1
        #             pass
        #         elif nums[k] - nums[j] > diff:
        #             j += 1
        #             pass
        #         else:
        #             ans += 1
        #             k += 1
        #             j += 1
        #             i += 1
        #             pass
        # return ans
        
        #### Improved Brute Force n * 3 ####
        ans, l = 0, len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                if nums[j] - nums[i] == diff:
                    for k in range(j + 1, l):
                        if nums[k] - nums[j] == diff:
                            ans += 1
                            break
                    break
        return ans
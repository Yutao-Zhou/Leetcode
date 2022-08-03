class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #### brute force ####
        # nums = sorted(nums)
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 ans.append((nums[i], nums[j], nums[k]))
        # return set(ans)
        
        #### sort ####
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i - 1]:
                pass
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r and nums[i] + nums[l] <= 0:
                    if nums[l] == nums[l - 1] and l - 1 != i:
                        l += 1
                    elif nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                    elif nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    else:
                        ans.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
        return ans
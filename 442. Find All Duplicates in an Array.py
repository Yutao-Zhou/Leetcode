class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
            #### Sort ####
            # ans = []
            # nums.sort()
            # for i in range(1, len(nums)):
            #     if nums[i] == nums[i - 1]:
            #         ans.append(nums[i])
            # return ans
            
            #### Hash on Original Array ####
            # ans = []
            # for c in nums:
            #     if nums[abs(c) - 1] < 0:
            #         ans.append(abs(c))
            #     nums[abs(c) - 1] *= -1
            # return ans
            
            #### Jump around ####
            ans, jump = [], 0
            for i in range(len(nums)):
                if nums[i] != 0 and nums[i] != -1:
                    jump = nums[i]
                    nums[i] = 0
                    while nums[jump - 1] != 0 and nums[jump - 1] != -1:
                        newJump = nums[jump - 1]
                        nums[jump - 1] = -1
                        jump = newJump
                    if nums[jump - 1] == -1:
                        ans.append(jump)
                    if nums[jump - 1] == 0:
                        nums[jump - 1] = -1
            return ans
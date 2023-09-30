class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #### Backtrack ####
        # def search(start, score, delete):
        #     if start == len(nums) or delete == 2:
        #         if delete == 0:
        #             return score - 1
        #         return score
        #     elif nums[start] == 0:
        #         ans = search(start + 1, score, delete + 1)
        #     else:
        #         ans = search(start + 1, score + 1, delete)
        #     return ans

        # ans = 0
        # for i in range(len(nums)):
        #     ans = max(ans, search(i, 0, 0))
        # return ans
        
        #### DP ####
        continuous = [0] * len(nums)
        deleted = [0] * len(nums)
        if nums[0] == 1:
            continuous[0] = 1
        
        for i in range(1, len(nums)):
            if nums[i] == 1:
                continuous[i] = continuous[i - 1] + 1
                deleted[i] = deleted[i - 1] + 1
            else:
                continuous[i] = 0
                deleted[i] = continuous[i - 1]
        return max(deleted)
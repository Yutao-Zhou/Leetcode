class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #### messy loop ######
#         ans = []
#         if len(nums) < 2:
#             for i in nums:
#                 ans.append(str(i))
#             return ans
#         i = 1
#         start = nums[0]
#         end = nums[0]
#         while 1:
#             if i == len(nums) - 1:
#                 if nums[i] - 1 == nums[i - 1]:
#                     end = nums[i]
#                     if start == end:
#                         ans.append(str(start))
#                     else:
#                         ans.append(str(start) + "->" + str(end))
#                 else:
#                     end = nums[i - 1]
#                     if start != end:
#                         ans.append(str(start) + "->" + str(end))
#                     if start == end:
#                         ans.append(str(end))
#                     ans.append(str(nums[i]))
#                 break 
#             if nums[i] - 1 == nums[i - 1]:
#                 end = nums[i]
#             if nums[i] - 1 != nums[i - 1]:
#                 end = nums[i - 1]
#                 if start == end:
                    
#                     ans.append(str(start))
#                     start = nums[i]
#                     end = nums[i]
#                 else:
#                     ans.append(str(start) + "->" + str(end))
#                     start = nums[i]
#                     end = nums[i]
#             i += 1
#        return ans
        
        ###### shorter two pointer #######
        i = 0
        j = 1
        ans = []
        if len(nums) < 2:
            for i in nums:
                ans.append(str(i))
            return ans
        nums.append(2 ** 32)
        while 1:
            if j == len(nums):
                return ans
            if nums[j] == nums[j - 1] + 1:
                j += 1
            elif nums[j] != nums[j - 1] + 1:
                if i == j - 1:
                    ans.append(str(nums[i]))
                    i = j
                    j += 1
                else:
                    ans.append(str(nums[i]) + "->" + str(nums[j - 1]))
                    i = j
                    j += 1
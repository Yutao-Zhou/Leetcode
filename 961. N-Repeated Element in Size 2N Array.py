class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        #### dictionary ####
        # frequency = {}
        # for i in nums:
        #     if i in frequency:
        #         frequency[i] += 1
        #     if i not in frequency:
        #         frequency[i] = 1
        # for freq in frequency.items():
        #     if freq[1] == len(nums) // 2:
        #         return freq[0]
        
        #### sort, possision ####
        # freq = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1,len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        # for num in nums:
        #     if num == nums[len(nums) // 2 - 1]:
        #         freq += 1
        # if freq == len(nums) // 2:
        #     return nums[len(nums) // 2 - 1]
        # return nums[len(nums) // 2]
        
        #### faster sort ####
        # freq = 0
        # nums.sort()
        # for num in nums:
        #     if num == nums[len(nums) // 2 - 1]:
        #         freq += 1
        # if freq == len(nums) // 2:
        #     return nums[len(nums) // 2 - 1]
        # return nums[len(nums) // 2]
        
        #### math ####
        return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))
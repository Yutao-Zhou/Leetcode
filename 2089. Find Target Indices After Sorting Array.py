class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        #### bubble sort ####
        # ans = []
        # for i in range(len(nums)):
        #     for j in range(0, len(nums) - i - 1):
        #         if nums[j] > nums[j + 1] :
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         ans.append(i)
        # return ans
        
        #### selection sort my way####
        # sort = []
        # minimum = 101
        # interation = 0
        # ans = []
        # while nums != []:
        #     for i in nums:
        #         if i < minimum:
        #             minimum = i
        #     sort.append(minimum)
        #     nums.remove(minimum)
        #     minimum = 101
        #     interation += 1
        # for i in range(len(sort)):
        #     if sort[i] == target:
        #         ans.append(i)
        # return ans
        
        #### counting without sort ####
        start = 0
        hit = 0
        for number in nums:
            if number < target:
                start += 1
            if number == target:
                hit += 1
        return range(start,start + hit)
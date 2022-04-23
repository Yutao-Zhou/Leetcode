class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        #### separate and recreat ####
        # odd = []
        # even = []
        # ans = []
        # for n in nums:
        #     if n % 2 == 0:
        #         even.append(n)
        #     if n % 2 == 1:
        #         odd.append(n)
        # for i in range(len(even)):
        #     ans.append(even[i])
        #     ans.append(odd[i])
        # return ans
        
        #### two pointer ####
        # i = 0
        # j = 0
        # ans = []
        # while i < len(nums) and j < len(nums):
        #     if nums[i] % 2 == 0:
        #         i += 1
        #     if nums[j] % 2 == 1:
        #         j += 1
        #     if nums[i] % 2 == 1 and nums[j] % 2 == 0:
        #         ans.append(nums[j])
        #         ans.append(nums[i])
        #         i += 1
        #         j += 1
        # return ans
        
        #### two pointer inplace ###
        i = 0
        j = i + 1
        while i < len(nums):
            if i % 2 == 0:
                if nums[i] % 2 == 1:
                    while nums[j] % 2 != 0:
                        j += 1
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    i += 1
                    j = i + 1
            if i % 2 == 1:
                if nums[i] % 2 == 0:
                    while nums[j] % 2 != 1:
                        j += 1
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    i += 1
                    j = i + 1      
        return nums
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ###### bad solution ####
        cach1 = 0
        cach2 = 0
        cach3 = 0
        for i in nums:
            print(cach1,cach2,cach3)
            if nums != cach1 and nums != cach2 and nums != cach3:
                if i > cach1:
                    if cach1 > cach2:
                        cach2 = cach1
                    cach1 = i
                elif i > cach2:
                    if cach2 > cach3:
                        cach3 = cach2
                    cach2 = i
                elif i > cach3:
                    cach3 = i
            print(cach1,cach2,cach3)
        if len(set(nums)) < 3:
            return cach1
        else:
            return cach3
        
        ###### set and sort not doing the problem#######
        # nums = set(nums)
        # nums = list(nums)
        # nums.sort()
        # print(nums)
        # if len(nums) < 3:
        #     return nums[-1]
        # else:
        #     return nums[-3]
        
        ##### bubble sort algorism #######
        # for i in range(len(nums)):
        #     already_sorted = True
        #     for j in range(len(nums) - i - 1):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #             already_sorted = False
        #     if already_sorted:
        #         break
        # ck = []
        # for i in range(-1,-len(nums)-1,-1):
        #     if nums[i] not in ck:
        #         ck.append(nums[i])
        # if len(ck) < 3:
        #     return ck[0]
        # else:
        #     return ck[2]
        
        
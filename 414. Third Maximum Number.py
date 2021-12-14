   
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ###### bad solution ####
        cach = [-2 ** 33,-2 ** 33,-2 ** 33]
        for i in nums:
            if i != cach[0] and i != cach[1] and i != cach[2]:
                if i > cach[0]:
                    cach.insert(0,i)
                    cach.pop()
                elif i > cach[1]:
                    cach.insert(1,i)
                    cach.pop()
                elif i > cach[2]:
                    cach.insert(2,i)
                    cach.pop()
        if len(set(nums)) < 3:
            return cach[0]
        else:
            return cach[2]
        
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
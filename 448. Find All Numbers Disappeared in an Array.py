class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # l = len(nums)
        # nums = set(nums)
        # ck = set(range(1,l + 1))
        # return ck.difference(nums)
        
        # ans = []
        # for i in range(1,len(nums) + 1):
        #     if i not in nums:
        #         ans.append(i)
        # return ans
        
        # nums.sort()
        # ans = []
        # i = 0
        # nums.append(len(nums) + 1)
        # nums.insert(0,0)
        # while 1:
        #     if i == len(nums) - 1:
        #         break
        #     if nums[i] != nums[i + 1] - 1 and nums[i] != nums[i + 1]:
        #         ans += (range(nums[i] + 1,nums[i + 1]))
        #     i += 1
        # return ans
        
        nums.sort()
        nums.append(len(nums) + 1)
        ans = [*range(1,len(nums) + 1)]
        i = 0
        j = 0
        while 1:
            if i == len(nums) or j == len(nums):
                break
            if nums[i] > ans[j]:
                j += 1
            if nums[i] < ans[j]:
                i += 1
            if nums[i] == ans[j]:
                ans.pop(j)
                i += 1
        return ans
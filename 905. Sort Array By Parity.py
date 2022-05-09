class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #### brute force ####
        # ans = deque()
        # for n in nums:
        #     if n % 2 == 0:
        #         ans.appendleft(n)
        #     if n % 2 == 1:
        #         ans.append(n)
        # return ans
        
        #### inplace ####
        if len(nums) == 1:
            return nums
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] % 2 == 1 and nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                pass
            elif nums[i] % 2 == 0:
                i += 1
                pass
            elif nums[j] % 2 == 1:
                j -= 1
                pass
        return nums
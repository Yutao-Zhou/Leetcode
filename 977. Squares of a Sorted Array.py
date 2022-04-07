class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #### simulationa and insert ####
        # ans = deque([nums[0] ** 2])
        # for i in range(1, len(nums)):
        #     if ans[-1] <= nums[i] * nums[i]:
        #         ans.append(nums[i] * nums[i])
        #         pass
        #     for j in range(len(ans)):
        #         if ans[j] > nums[i] * nums[i]:
        #             ans.insert(j, nums[i] * nums[i])
        #             break
        # return ans
        
        #### two pointer ####
        ans = deque()
        i = 0
        j = len(nums) - 1
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                ans.appendleft(nums[i] ** 2)
                i += 1
            else:
                ans.appendleft(nums[j] ** 2)
                j -= 1
        return ans
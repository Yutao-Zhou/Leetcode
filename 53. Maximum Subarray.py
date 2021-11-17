class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for i in range(1,len(nums)):
                t = ans[-1] + nums[i]
                if t > nums[i] :
                    ans.append(t)
                else:
                    ans.append(nums[i])
                    pass
        return max(ans)          
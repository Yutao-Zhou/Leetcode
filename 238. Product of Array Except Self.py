class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #### prefix suffix####
        # prefix = [1]
        # suffix = [1]
        # for n in nums:
        #     prefix.append(prefix[-1] * n)
        # prefix = prefix[1 : -1]
        # for i in range(-1, -len(nums) - 1, -1):
        #     suffix.append(suffix[-1] * nums[i])
        # suffix = suffix[1 : -1]
        # ans = [suffix[-1]] + prefix
        # for i in range(1, len(ans) - 1):
        #     ans[i] *= suffix[-i - 1]
        # return ans
        
        #### answer array ####
        # presuffix = 1
        # ans = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     ans[i] = ans[i - 1] * nums[i - 1]
        # for i in range(-1, -len(nums) - 1, -1):
        #     ans[i] *= presuffix
        #     presuffix *= nums[i]
        # return ans
        
        #### start at same time ####
        ans = [1] * len(nums)
        left, right = 1, 1
        for i in range(len(nums)):
            ans[i] *= left
            ans[~i] *= right
            left *= nums[i]
            right *= nums[~i]
        return ans
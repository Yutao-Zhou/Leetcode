class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #### brute force ####
        # i = 0
        # ans = -(10 ** 5)
        # cach = 0
        # for j in range(len(nums)):
        #     cach = 0
        #     for k in range(i,j + 1):
        #         cach += nums[k]
        #     if cach < 0:
        #         i = j + 1
        #     if cach >= ans:
        #         ans = cach
        # return ans
        
        #### compare each one -- time limit exceed ####
        # ans = [nums[0]]
        # for i in range(1,len(nums)):
        #         t = ans[-1] + nums[i]
        #         if t > nums[i] :
        #             ans.append(t)
        #         else:
        #             ans.append(nums[i])
        #             pass
        # return max(ans)
        
        #### greedy ####
        # ans = -10000
        # cache = 0
        # for n in nums:
        #     cache += n
        #     if cache > ans:
        #         ans = cache
        #     if cache < 0:
        #         cache = 0
        # return ans
        
        #### divide and conquer ####
        def maxSubArray(nums, L, R):
            if L > R:
                return -inf
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid-1, L-1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + nums [i])
            cur_sum = 0
            for i in range(mid+1, R+1):
                right_sum = max(right_sum, cur_sum := cur_sum + nums [i])
            return max(maxSubArray(nums , L, mid-1), maxSubArray(nums , mid+1, R), left_sum + nums[mid] + right_sum)
        return maxSubArray(nums, 0, len(nums)-1)
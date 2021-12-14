class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ####### force #########
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
        
        ########### compare each one ###########
        ans = [nums[0]]
        for i in range(1,len(nums)):
                t = ans[-1] + nums[i]
                if t > nums[i] :
                    ans.append(t)
                else:
                    ans.append(nums[i])
                    pass
        return max(ans)  
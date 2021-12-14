class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ##### force solve #####
        # i = 0
        # r = 1
        # ans = 0
        # while r <= len(arr):
        #     if i + r == len(arr) + 1:
        #         i = 0
        #         r += 2
        #     else:
        #         s = arr[i:i + r]
        #         i += 1
        #         ans += sum(s)
        # return ans
        
        #### math #####
        ans = 0
        for i in range(len(arr)):
            ans += (((len(arr) - i) * (i + 1) + 1 ) // 2) * arr[i]
        return ans
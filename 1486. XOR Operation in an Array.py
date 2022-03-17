class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        #### simulation ####
        # arr = []
        # for i in range(n):
        #     arr.append(start + 2 * i)
        # ans = arr[0]
        # for i in range(1,len(arr)):
        #     ans ^= arr[i]
        # return ans
       
        #### functional brain ####
        ans = start
        for i in range(1, n):
            ans ^= start + 2 * i
        return ans
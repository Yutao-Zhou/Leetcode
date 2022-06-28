class Solution:
    def minOperations(self, n: int) -> int:
        #### simulate without thinking ####
        # array = []
        # ans = 0
        # for i in range(n):
        #     array.append((2 * i) + 1)
        # target = sum(array) // len(array)
        # for i in range(len(array) // 2):
        #     ans += target - array[i]
        # return ans
        
        #### math ####
        mid = n // 2
        if n % 2:
            center = 2 * mid + 1
            return (center - 1) * (mid + 1) // 2
        else:
            center = 2 * mid
            return center * mid // 2
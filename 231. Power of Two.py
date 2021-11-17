class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # else:
        #     while 1:
        #         if n == 1:
        #             return True
        #         if n % 2 == 1 and n != 1:
        #             return False
        #         n /= 2
        
        return n > 0 and not (n & n-1)
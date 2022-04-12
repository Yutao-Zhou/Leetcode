class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #### loop and check ####
        # if n <= 0:
        #     return False
        # else:
        #     while 1:
        #         if n == 1:
        #             return True
        #         if n % 2 == 1 and n != 1:
        #             return False
        #         n /= 2
        
        #### trick ####
        # return n > 0 and not (n & n-1)
        
        #### recursive ####
        if n < 1:
            return False
        def recursive(n):
            if n == 1:
                return True
            elif n % 2:
                return False
            else:
                return recursive(n // 2)
        return recursive(n)
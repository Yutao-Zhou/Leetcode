class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #### loop ####
        # if n < 1:
        #     return False
        # while n > 2:
        #     if n % 3:
        #         return False
        #     n = n // 3
        # return n == 1
        
        #### recursive ####
        def recursive(n):
            if n == 1:
                return True
            if n % 3:
                return False
            else:
                return recursive(n // 3)
        if n < 1:
            return False
        return recursive(n)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #### loop ####
        # if n < 1:
        #     return False
        # while n > 3:
        #     if n % 4:
        #         return False
        #     n = n // 4
        # return n == 1
        
        #### recursive ####
        def recursive(num):
            if num == 4 or num == 1:
                return True
            if num % 4 != 0:
                return False
            return recursive(num // 4)
        if n < 1:
            return False
        return recursive(n)
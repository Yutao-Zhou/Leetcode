class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #### loop ####
        if n < 1:
            return False
        while n > 3:
            if n % 4:
                return False
            n = n // 4
        return n == 1
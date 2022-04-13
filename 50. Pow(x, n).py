class Solution:
    def myPow(self, x: float, n: int) -> float:
        #### recursive without math ####
        # import sys
        # sys.setrecursionlimit(2147483647)
        # if n < 0:
        #     n = abs(n)
        #     x = 1 / x
        # X = x
        # def recursion(x, n):
        #     if abs(x) < 1e-40: return 0
        #     if n == 0:
        #         return float(1)
        #     if n <= 1:
        #         return x
        #     return recursion(x * X, n - 1)
        # return recursion(x, n)
        
        #### optimized recursive ####
        # if n < 0:
        #     n = abs(n)
        #     x = 1 / x
        # X = x
        # def recursion(x, n):
        #     if abs(x) < 1e-40:
        #         return 0 
        #     if n == 0:
        #         return 1
        #     if n % 2 == 0:
        #         return recursion(x, n // 2) * recursion(x, n // 2)
        #     if n % 2 == 1:
        #         return  recursion(x, n // 2) * recursion(x, n // 2) * x
        # return recursion(x, n)
        
        #### iteritive ####
        if n < 0:
            n = abs(n)
            x = 1 / x
        ans = 1
        while n:
            if n % 2:
                ans *= x
            x *= x
            n //= 2
        return ans
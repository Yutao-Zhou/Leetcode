class Solution:
    def fib(self, n: int) -> int:
    ##### raw solve ####
    #     cach1 = 0
    #     cach2 = 1
    #     ans = 0
    #     i = 2
    #     if n < 2:
    #         return n
    #     else:
    #         while i <= n:
    #             ans = cach1 + cach2
    #             cach1 = cach2
    #             cach2 = ans
    #             i += 1
    #     return ans
    
    #### math #####
        Phi = (1 + 5 ** 0.5) / 2
        phi = (1 - 5 ** 0.5) / 2
        return int((Phi ** n - phi ** n) / 5 ** 0.5)